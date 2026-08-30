CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts
USING fts5(
  id UNINDEXED,
  question,
  answer,
  stack,
  category,
  sub_category,
  tags,
  language UNINDEXED,
  library_url UNINDEXED,
  source_path UNINDEXED,
  has_images UNINDEXED,
  images_text,
  images UNINDEXED,
  score UNINDEXED,
  updated_at UNINDEXED,
  tokenize='porter unicode61 remove_diacritics 2'
);
