# SQL EXECUTION PLAN

## Common Operators

### Data Access Operators:

- Index Scan:
  - What it is: The database engine reads through the entire leaf level of an index to retrieve the necessary data.
  - When it happens:
    - When the query needs a large portion of the data in the table, and the index covers the required columns.
    - When there's no suitable index for the query's WHERE clause, and the optimizer chooses to scan an existing index rather than the entire table (Heap Scan).
    - On small tables where the cost of a seek might be higher than a full scan.
  - Performance implications: Can be expensive if the index is large and the query only needs a small subset of data. It's generally less efficient than an Index Seek for selective queries.
  - Graphical representation: Often depicted as a cylindrical icon labeled "Index Scan".

- Index Seek:
  - What it is: The database engine uses the B-tree structure of an index to directly locate the specific rows that satisfy the query's WHERE clause. It navigates the index levels to pinpoint the relevant data pages.
  - When it happens: When the query has a WHERE clause that matches the leading columns of an available index. This allows the engine to "seek" directly to the relevant part of the data.
  - Performance implications: Highly efficient for selective queries as it minimizes the number of data pages that need to be read.
  - Graphical representation: Often depicted as a cylindrical icon labeled "Index Seek".

- Clustered Index Seek:
  - What it is: Similar to a regular Index Seek, but specifically performed on the clustered index of a table. Since the clustered index is the data, the seek directly locates the data rows.
  - When it happens: When the WHERE clause matches the clustered index key (often the primary key) or a prefix of it.
  - Performance implications: Very efficient for retrieving specific rows based on the clustered key.   
  - Graphical representation: Depicted as a cylindrical icon labeled "Clustered Index Seek". 

### Join Operators:

- Nested Loops:
  - What it is: A join algorithm where the database engine iterates through each row of the "outer" table and, for each of those rows, it searches for matching rows in the "inner" table.
  - When it happens:
    - Often used when one of the tables in the join is small, and there's an efficient way to look up matching rows in the other table (e.g., using an index).
    - Can be the only option for certain types of joins (like CROSS JOIN or some complex OUTER APPLY).
  - Performance implications: Can be very inefficient if both tables are large and there isn't a suitable index on the inner table's join column, as it can lead to a large number of reads on the inner table.
  - Graphical representation: Typically shown as a loop-like icon labeled "Nested Loops".

### Post-Retrieval Operators:

- Key Lookup:
  - What it is: Occurs after an Index Seek on a non-clustered index. If the non-clustered index doesn't contain all the columns required by the query (e.g., in the SELECT list), the engine needs to go back to the clustered index (using the clustered key obtained from the non-clustered index) to fetch the missing columns.
  - When it happens: When a non-clustered index efficiently helps filter rows, but doesn't "cover" all the necessary columns for the query's output.
  - Performance implications: Can be expensive, especially if a large number of rows are retrieved from the non-clustered index, as each row might require a separate lookup in the clustered index (which involves additional I/O).
  - Graphical representation: Usually depicted as a small key icon connected to a Nested Loops Join (where the outer input is the result of the Index Seek and the inner input is the clustered index).
- Stream Aggregate:
  - What it is: An aggregate function (like SUM, AVG, COUNT, MIN, MAX) is computed over a sorted input stream of data. The data must be sorted on the grouping columns (if a GROUP BY clause is present).
  - When it happens: When the query includes aggregate functions and the input data is already sorted (either due to an index or a Sort operator in the plan).
  - Performance implications: Generally efficient because it processes the sorted data sequentially and doesn't require holding intermediate results in memory for the entire dataset.
  - Graphical representation: Often shown as an icon with a summation symbol (Σ) or a similar aggregation symbol, labeled "Stream Aggregate".
- Compute Scalar:
  - What it is: Performs a scalar computation. This could involve evaluating an expression, converting data types, or performing other row-level calculations.   
  - When it happens: When the query includes calculated columns, functions in the SELECT, WHERE, ORDER BY, or GROUP BY clauses, or implicit data type conversions.
  - Performance implications: The cost depends on the complexity of the computation. Simple scalar operations usually have a minimal impact. Complex calculations or conversions on a large number of rows can add overhead.
  - Graphical representation: Typically shown as a small box with a mathematical symbol or the label "Compute Scalar".

