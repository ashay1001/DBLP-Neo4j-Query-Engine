//Index creation on COAUTHOR relation
CREATE FULLTEXT INDEX articleIndex FOR ()-[r:COAUTHOR]-() ON EACH [r.title]