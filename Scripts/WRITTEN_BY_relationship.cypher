//WRITTEN_BY relationship
match(n:Article)
unwind n.authors as author
merge (b:Author{name:author})
merge (n)-[:WRITTEN_BY]->(b)