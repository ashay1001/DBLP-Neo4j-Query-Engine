//Graph Projection with COAUTHOR
CALL gds.graph.create(
  'coauthors_rank',
  ['Author'],
  'COAUTHOR')
YIELD
  graphName AS graph, nodeProjection, nodeCount AS nodes,  relationshipCount AS rels