//COUTHOR Relationship Import
CALL apoc.periodic.iterate(
  'UNWIND ["dblp-ref-3.json"] as file 
   CALL apoc.load.json("./" + file) 
   yield value return value',
  'MERGE (a:Author{name:value.authors[0]}) 
   WITH a,value.authors as authors,value.title as t,value.id as art_id 
   UNWIND authors as author 
   MERGE (b:Author{name:author}) 
   MERGE (b)-[:COAUTHOR{title:t, id:art_id}]->(a)'
,{batchSize: 10000, iterateList: true})