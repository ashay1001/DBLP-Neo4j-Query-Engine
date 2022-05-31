//Create Unique Constraint
CALL apoc.schema.assert(
{},
{Article:['index'],Author:['name']})