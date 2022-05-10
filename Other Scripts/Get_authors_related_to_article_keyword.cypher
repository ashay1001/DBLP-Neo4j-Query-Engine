//Get authors related to article keyword
CALL db.index.fulltext.queryNodes("articlesAll", "EBG")
YIELD node
with node.title as titles
unwind titles as title
match (n:Article)-[:WRITTEN_BY]->(p:Author) where n.title = title
return id(p) as id, n.title as title1, p.name as name