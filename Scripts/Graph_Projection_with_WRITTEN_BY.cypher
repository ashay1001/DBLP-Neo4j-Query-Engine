//Graph Projection with WRITTEN_BY
//Creating Graph Projection
CALL gds.graph.create(
  'authorsRank1',
  ['Author','Article'],
  'WRITTEN_BY')
YIELD
  graphName AS graph, nodeProjection, nodeCount AS nodes,  relationshipCount AS rels