//Page Rank with write
CALL gds.pageRank.write('authorsRank1',
{maxIterations: 20,
writeProperty: 'pgrank_wb_authors'
})
YIELD nodePropertiesWritten, ranIterations