//QUERY 3
CALL db.index.fulltext.queryNodes("articlesAll", "EBG")
yield node with collect(node.authors) as authors unwind authors as author
unwind author as name
match (n)-[:WRITTEN_BY]-(m:Author) where m.name=name return distinct m.name as Author, m.pgrank_wb_authors as Page_Rank order by Page_Rank desc