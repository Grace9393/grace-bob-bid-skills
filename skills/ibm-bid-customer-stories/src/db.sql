-- IBM Customer Stories Database Schema
-- FTS5 table with porter stemming for full-text search

CREATE VIRTUAL TABLE IF NOT EXISTS stories_fts USING fts5(
    title,
    company,
    industry,
    clouds_implemented,
    description,
    outcomes,
    source,
    links UNINDEXED,
    tokenize = 'porter unicode61 remove_diacritics 2'
);