//Full text search on COAUTHOR relation
CALL db.index.fulltext.queryRelationships("articleIndex", "Social Networks") YIELD relationship, score
RETURN relationship, score