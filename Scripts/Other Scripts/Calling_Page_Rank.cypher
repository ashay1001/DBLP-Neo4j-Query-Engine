//Calling Page Rank
CALL gds.pageRank.stream('authorsRank1')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC