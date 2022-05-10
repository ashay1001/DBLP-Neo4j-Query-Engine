// Deleting Self Loops
MATCH (a:Author)-[rel:COAUTHOR]->(a) 
DELETE rel;