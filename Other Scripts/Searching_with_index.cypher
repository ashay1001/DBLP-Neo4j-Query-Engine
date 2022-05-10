//Searching with index
CALL db.index.fulltext.queryNodes("articlesAll", "social networks")
YIELD node, score
with node.title as titles, score
unwind titles as title
return title, score