# Query Optimization

## Observed Operations in the Execution Plan:

1. Nested Loops
1. Index Seek
1. Key Lookup
1. Sort
1. Filter
1. Compute Scalar
1. Segment Project


## Performance Improvement Strategies:

1. Minimize Key Lookups
    - Key lookups can be expensive. Consider using covering indexes that include all the columns needed by the query to avoid extra lookups.
1. Optimize Nested Loops
    - Nested loops are efficient for small datasets but can be slow for large joins. If large datasets are involved, consider merge joins or hash joins by rewriting the query or using query hints.
1. Improve Indexing Strategy
    - Ensure indexes exist on:
        - Join keys
        - Filtered columns
        - Sorted columns
    - Use included columns in indexes to cover more of the query.
1. Reduce Sort Operations
    - Sorting is expensive. If possible, pre-sort data using indexes or avoid unnecessary ORDER BY clauses.
1. Review Filters and Predicates
    - Ensure filters are sargable (Search ARGument ABLE), meaning they can use indexes. Avoid functions on columns in WHERE clauses (e.g., WHERE YEAR(date) = 2023).
1. Analyze Execution Plan Cost
    - Use SQL Server Management Studio (SSMS) to view estimated vs. actual execution plans and identify the most expensive steps.
1. Update Statistics and Rebuild Indexes
    - Outdated statistics can mislead the optimizer. Use:
       - update statistics tableName; alter index all on tableName rebuild;
1. Use Query Hints Carefully
    - In some cases, hints like OPTION (HASH JOIN) or OPTION (RECOMPILE) can help, but use them only after testing.
1. Avoid SELECT *
    - Always specify only the columns you need to reduce I/O and memory usage.
1. Consider Query Refactoring
    - Break complex queries into CTEs or temporary tables to simplify execution and improve plan reuse.

## Problems 

1. Large Number of Rows Processed and High Percentages:
    - Many operators are processing a very high percentage of rows (e.g., Nested Loops, Filter, Index Scan). This suggests a lack of selectivity early in the query, leading to a lot of unnecessary work.
1. Recommendations:
    - Indexes, Indexes, Indexes! This is the most crucial aspect. The plan shows Index Scan (Nonclustered) and Clustered Index Seek. While these are good, we need to ensure the right indexes exist and are being used effectively.
    - Focus on JOIN and WHERE clauses: Identify the columns used in your JOIN conditions and WHERE clauses (especially those with Filter operators). Create non-clustered indexes on these columns.
    - Covering Indexes: If your query frequently retrieves a few specific columns, consider creating covering indexes. A covering index includes all the columns needed for the query, so SQL Server doesn't have to go to the base table to retrieve additional data. This would be particularly useful for the Index Scan (Nonclustered) operations.
    - Index on tbl_Patient_Insurance: The Index Scan (Nonclustered) on tbl_Patient_Insurance is processing 95,153,929 rows, which is a huge number. This table clearly needs an effective index.
    - Index on tbl_Exams: The Index Seek (Nonclustered) on tbl_Exams is performing well, but the subsequent Key Lookup (Clustered) suggests that the non-clustered index isn't covering all the columns needed. Consider adding the looked-up columns to the non-clustered index as INCLUDE columns.
1. Nested Loops Joins (Left Outer Join) on Large Datasets:
    - While Nested Loops can be efficient for small outer inputs and a good index on the inner input, when the outer input is large (as suggested by the high row counts after the Merge Join), they can become very expensive.
1. Recommendations:
    - Ensure Proper Indexing: As mentioned above, make sure the inner table of the Nested Loops join has an appropriate index on the join column(s). If it's a large table, a well-structured index is critical.
    - Consider Hash or Merge Joins: SQL Server might choose Nested Loops because it believes it's the most efficient. However, if the data distribution or index selectivity changes, a Hash or Merge Join might be better. While you generally let the optimizer decide, if you've exhausted indexing options, you could hint for a different join type (though this is usually a last resort).
1. Filter Operators Processing Many Rows:

Multiple Filter operators are processing a large number of rows before significantly reducing them. This means data is being retrieved and processed unnecessarily before being discarded.

Recommendations:

Push Down Predicates: Ensure your WHERE clauses are as restrictive as possible and are applied early in the query. SQL Server usually does this, but sometimes complex logic can prevent it.
Indexing on Filtered Columns: Create indexes on the columns used in your WHERE clauses to allow for efficient filtering using index seeks.
Computed Columns: If you are filtering on a complex expression, consider creating a persisted computed column and indexing that column.
4. Table Scans (Index Scan (Nonclustered)) on Large Tables:

The Index Scan (Nonclustered) on tbl_Patient_Insurance is particularly concerning due to the huge number of rows processed. An index scan reads every row in the index, which is inefficient if you only need a small subset of the data.

Recommendations:

Targeted Indexes: Create a more specific index that SQL Server can use for an Index Seek instead of a Scan. This index should be on the columns used in the WHERE clause or JOIN conditions related to tbl_Patient_Insurance.
5. Sort Operator:

A Sort operator can be expensive, especially on large datasets.

Recommendations:

Order By and Indexes: If the Sort is due to an ORDER BY clause, consider creating an index that includes the ORDER BY columns in the correct order. This can allow SQL Server to retrieve the data already sorted, eliminating the need for a separate sort operation.
Group By and Indexes: If the Sort is due to a GROUP BY clause, a composite index on the GROUP BY columns can often help.
6. Key Lookup (Clustered):

The Key Lookup (Clustered) after the Index Seek (Nonclustered) on tbl_Exams indicates that the non-clustered index being used doesn't contain all the columns needed by the query. SQL Server has to perform an extra lookup into the clustered index (the actual data rows) to get the missing columns.

Recommendations:

Covering Index: Modify the non-clustered index on tbl_Exams to include the columns that are being looked up. You can do this using the INCLUDE keyword when creating or altering the index. For example:
SQL

CREATE NONCLUSTERED INDEX IX_YourIndexName ON tbl_Exams (indexed_column) INCLUDE (column1, column2, column3);
Replace indexed_column with the column(s) already in your index and column1, column2, column3 with the columns being looked up.
General Strategies:

Analyze the Actual Query: Without the actual SQL query, these are general recommendations based on the plan. Review your SELECT, FROM, JOIN, WHERE, GROUP BY, and ORDER BY clauses to identify the exact columns involved.
Statistics: Ensure your database statistics are up-to-date. Outdated statistics can lead the optimizer to make poor choices about query plans.
SQL

UPDATE STATISTICS YourTableName;
-- Or for all tables in the database
EXEC sp_updatestats;
Database Design: While usually a long-term solution, sometimes the fundamental database design (e.g., lack of proper relationships, denormalization where normalization would be better, or vice-versa) can be a root cause.
Parameter Sniffing: If this query is part of a stored procedure, be aware of parameter sniffing. Sometimes, the initial plan generated for a specific parameter value might not be optimal for subsequent, different parameter values.
Execution Plan Analysis Tools: Use SQL Server Management Studio (SSMS) to view the actual execution plan. Hover over each operator to see detailed information (number of rows, estimated vs. actual, CPU/I/O costs). The "Properties" window for each operator provides even more detail.
By systematically addressing these points, focusing heavily on appropriate indexing and ensuring predicates are applied early, you should see significant improvements in your query's performance.