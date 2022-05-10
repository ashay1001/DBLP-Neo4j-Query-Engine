//Import Data
CALL apoc.periodic.iterate(
  'UNWIND ["dblp-ref-3.json"] as file 
   CALL apoc.load.json("./" + file) 
   yield value return value',
  'MERGE (a:Article{index:value.id}) 
   ON CREATE SET a += apoc.map.clean(value,["id","authors","references"],[0]) 
   WITH a,value.authors as authors 
   UNWIND authors as author 
   MERGE (b:Author{name:author}) 
   MERGE (b)-[:AUTHOR]->(a)'
,{batchSize: 10000, iterateList: true})