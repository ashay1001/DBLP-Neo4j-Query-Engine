//Calling Page Rank on COAUTHER
CALL gds.pageRank.stream('coauthors_rank')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC