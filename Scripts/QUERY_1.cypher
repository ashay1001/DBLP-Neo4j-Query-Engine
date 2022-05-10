//QUERY 1
CALL db.index.fulltext.queryNodes("articlesAll", "social networks")
YIELD node, score
with node.title as titles, score
unwind titles as title
match (n:Article)<-[:AUTHOR]-(p) where n.title = title
return n.title as Article, p.name as Author, score as Score, p.degree_wb_authors/100 as Relevance order by Score,Relevance desc limit 250