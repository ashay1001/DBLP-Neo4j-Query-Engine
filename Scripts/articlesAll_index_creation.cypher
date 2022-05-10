//articlesAll index creation
CALL db.index.fulltext.createNodeIndex('articlesAll', 
  ['Article'], ['title', 'abstract'])