#!/usr/bin/env python3
"""
IBM Bid Qualification Calculator

Calculates qualification scores and generates recommendations for bid opportunities.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def load_criteria() -> List[Dict]:
    """Load qualification criteria from JSON file."""
    criteria_path = Path(__file__).parent.parent / "references" / "qualification_criteria.json"
    with open(criteria_path) as f:
        return json.load(f)


def calculate_score(scores: Dict[int, int]) -> int:
    """
    Calculate total qualification score.
    
    Args:
        scores: Dictionary mapping criterion number (1-20) to score (1-5)
    
    Returns:
        Total score out of 100
    """
    return sum(scores.values())


def get_recommendation(score: int) -> Tuple[str, str]:
    """
    Get recommendation based on total score.
    
    Args:
        score: Total qualification score
    
    Returns:
        Tuple of (decision, description)
    """
    if score <= 40:
        return "NO-BID", "High risk opportunity - recommend qualifying out"
    elif score <= 60:
        return "CONDITIONAL", "Medium risk - requires comprehensive mitigation strategy"
    elif score <= 80:
        return "PROCEED", "Good opportunity - proceed with appropriate caution"
    else:
        return "PRIORITISE", "Strong opportunity - prioritise resources and pursue aggressively"


def identify_red_flags(scores: Dict[int, int]) -> List[str]:
    """
    Identify critical red flag criteria.
    
    Args:
        scores: Dictionary mapping criterion number to score
    
    Returns:
        List of red flag descriptions
    """
    red_flags = []
    
    red_flag_criteria = {
        1: "Strong incumbent advantage",
        7: "Poor decision-maker relationships",
        18: "Budget misalignment",
        19: "Missing commercial framework",
        20: "High TUPE complexity"
    }
    
    for criterion_num, description in red_flag_criteria.items():
        if scores.get(criterion_num, 0) <= 2:
            red_flags.append(f"Criterion {criterion_num}: {description} (Score: {scores[criterion_num]})")
    
    return red_flags


def identify_strengths(scores: Dict[int, int], criteria: List[Dict]) -> List[str]:
    """
    Identify top scoring criteria as strengths.
    
    Args:
        scores: Dictionary mapping criterion number to score
        criteria: Full criteria structure
    
    Returns:
        List of top 3 strengths
    """
    # Get all criteria with scores 4-5
    strong_criteria = [(num, score) for num, score in scores.items() if score >= 4]
    # Sort by score descending
    strong_criteria.sort(key=lambda x: x[1], reverse=True)
    
    strengths = []
    for num, score in strong_criteria[:3]:
        # Find criterion details
        for category in criteria:
            for criterion in category['criteria']:
                if criterion['number'] == num:
                    strengths.append(f"Criterion {num}: {criterion['question'].strip()} (Score: {score})")
                    break
    
    return strengths


def identify_risks(scores: Dict[int, int], criteria: List[Dict]) -> List[str]:
    """
    Identify lowest scoring criteria as risks.
    
    Args:
        scores: Dictionary mapping criterion number to score
        criteria: Full criteria structure
    
    Returns:
        List of top 3 risks
    """
    # Get all criteria with scores 1-3
    weak_criteria = [(num, score) for num, score in scores.items() if score <= 3]
    # Sort by score ascending
    weak_criteria.sort(key=lambda x: x[1])
    
    risks = []
    for num, score in weak_criteria[:3]:
        # Find criterion details
        for category in criteria:
            for criterion in category['criteria']:
                if criterion['number'] == num:
                    risks.append(f"Criterion {num}: {criterion['question'].strip()} (Score: {score})")
                    break
    
    return risks


def calculate_category_scores(scores: Dict[int, int], criteria: List[Dict]) -> Dict[str, Dict]:
    """
    Calculate scores by category.
    
    Args:
        scores: Dictionary mapping criterion number to score
        criteria: Full criteria structure
    
    Returns:
        Dictionary mapping category ID to score details
    """
    category_scores = {}
    
    for category in criteria:
        cat_id = category['id']
        cat_name = category['name']
        criterion_scores = []
        
        for criterion in category['criteria']:
            num = criterion['number']
            if num in scores:
                criterion_scores.append(scores[num])
        
        total = sum(criterion_scores)
        max_possible = len(criterion_scores) * 5
        
        category_scores[cat_id] = {
            'name': cat_name,
            'score': total,
            'max': max_possible,
            'percentage': (total / max_possible * 100) if max_possible > 0 else 0
        }
    
    return category_scores


def main():
    """Main execution function for testing."""
    # Example scores for testing
    example_scores = {
        1: 3, 2: 4, 3: 4, 4: 3, 5: 4,
        6: 4, 7: 3, 8: 3, 9: 4, 10: 4,
        11: 4, 12: 3, 13: 3, 14: 3, 15: 3,
        16: 4, 17: 4, 18: 3, 19: 4, 20: 5
    }
    
    criteria = load_criteria()
    
    total_score = calculate_score(example_scores)
    decision, description = get_recommendation(total_score)
    red_flags = identify_red_flags(example_scores)
    strengths = identify_strengths(example_scores, criteria)
    risks = identify_risks(example_scores, criteria)
    category_scores = calculate_category_scores(example_scores, criteria)
    
    print(f"Total Score: {total_score}/100")
    print(f"Decision: {decision}")
    print(f"Description: {description}\n")
    
    print("Strengths:")
    for s in strengths:
        print(f"  - {s}")
    
    print("\nRisks:")
    for r in risks:
        print(f"  - {r}")
    
    print("\nRed Flags:")
    for rf in red_flags:
        print(f"  - {rf}")
    
    print("\nCategory Breakdown:")
    for cat_id, details in category_scores.items():
        print(f"  {cat_id}: {details['name']}")
        print(f"     Score: {details['score']}/{details['max']} ({details['percentage']:.1f}%)")


if __name__ == "__main__":
    main()
