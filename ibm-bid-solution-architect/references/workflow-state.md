# Workflow State File Contract

Use `../tmp/ibm-bid-solution/state.json` during generation.

Required shape:
```json
{
  "mode": "sectional",
  "current_section": "02-system-architecture",
  "completed_sections": [],
  "pending_sections": [],
  "changed_requirements": [],
  "dependencies_satisfied": {},
  "last_updated": "ISO-8601"
}
```

Also maintain:
- `../tmp/ibm-bid-solution/section-memory.md` (5-10 lines per completed section)
- `../tmp/ibm-bid-solution/sections/NN-<section-name>.md` (one file per section)
- `../tmp/ibm-bid-solution/complete_solution.md` (assembled output)
