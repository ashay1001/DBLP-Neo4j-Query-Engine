//Creating Graph Projection Initial
CALL gds.graph.create.cypher(
  'authorsRank',
  'MATCH (n:Author) RETURN id(n) AS id',
  'MATCH (n:Author)-[r:AUTHOR]->(m:Article) RETURN id(n) AS source, id(m) AS target',
  {validateRelationships:FALSE})
YIELD
  graphName AS graph, nodeQuery, nodeCount AS nodes, relationshipQuery, relationshipCount AS rels