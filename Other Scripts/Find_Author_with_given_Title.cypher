//Find Author with given Title
CALL db.index.fulltext.queryNodes("articlesAll", "social networks")
YIELD node, score
with node.title as titles, score
unwind titles as title
match (n:Article)<-[:AUTHOR]-(p) where n.title = title
return n.title, p.name, score limit 250