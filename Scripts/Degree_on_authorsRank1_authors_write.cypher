//Degree on authorsRank1 (authors) write
CALL gds.degree.write(
   'authorsRank1',
   { orientation: 'REVERSE',  writeProperty: 'degree_wb_authors' }
)
YIELD centralityDistribution, nodePropertiesWritten
RETURN centralityDistribution.min AS minimumScore, centralityDistribution.mean AS meanScore, nodePropertiesWritten