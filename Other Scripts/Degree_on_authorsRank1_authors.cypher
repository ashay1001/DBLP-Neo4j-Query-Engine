//Degree on authorsRank1 (authors)
CALL gds.degree.stream(
   'authorsRank1',
   { orientation: 'REVERSE' }
)
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score AS followees
ORDER BY followees DESC