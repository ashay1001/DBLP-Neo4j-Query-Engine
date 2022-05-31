//Page Rank on authorsRank1
CALL gds.pageRank.stream('authorsRank1')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score