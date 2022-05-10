//Degree on authorsRank1 (articles)
CALL gds.degree.stream('authorsRank1')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).title AS name, score AS followers
ORDER BY followers DESC, name DESC