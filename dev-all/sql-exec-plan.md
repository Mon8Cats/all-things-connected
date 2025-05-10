# Execution Plan

## Key Parts

- Object Clause:
  - specify the table and the PK
- Where Clause:
  - Filter the result based on several conditions


## Steps

- select count(*) 
- compute scalar:
  - Expr1005 = convert_implicit(int, [Expr1009], 0)
  - PhysicalOp = compute scalar, 
  - LogicalOp = compute scalar
- Stream Aggregate
  - Expr1009 = count(*)
  - PhysicalOp = Stream Aggregate
  - LogicalOp = Aggregate
- Merge join (inner join)
  - MERGE: pts.PK_DNUMBER = exams.FK_DNUMBER,
  - RESIDUAL: 
  - PhysicalOp: Merge Join
  - LogicalOp: Inner Join
- Clustered Index Scan (tbl_Patients) 
  - Object: (patient_table.pk_col) as [pts]), ordered forward
  - PhysicalOp: Clustered Index Scan
  - LogicalOp: Clustered Index Scan
- Sort
  - Order By: exams.fk_dnumber asc
  - PhysicalOp: Sort
  - LogicalOp: Sort
- Hash Match (Inner Join)
  - HASH: p1.PK_LOCID = exams.FK_LOCID
  - Residual:
  - PhysicalOp: Hash Match
  - Logical: Inner Join
- Clustered Index Scan (tbl_exams)
  - Object:
  - Where:
  - PhysicalOp
  - LogicalOp



Great question! Both Hash Match and Merge Join are physical operations used to perform an Inner Join in SQL Server, but they have different characteristics and are suited to different scenarios. Here's a comparison:

Hash Match
Algorithm: Uses a hash table to match rows from the two input tables.
When Used: Typically used when joining large tables or when there are no suitable indexes on the join columns.
Performance: Can be efficient for large datasets but may require significant memory to build the hash table.
Steps:
Build Phase: SQL Server creates a hash table for the smaller input table.
Probe Phase: SQL Server scans the larger input table and matches rows using the hash table.
Advantages: Good for large, unsorted datasets and when indexes are not available.
Disadvantages: Memory-intensive and can be slower if the hash table becomes too large.
Merge Join
Algorithm: Requires both input tables to be sorted on the join columns and then merges them.
When Used: Typically used when both input tables are already sorted or have suitable indexes on the join columns.
Performance: Very efficient for sorted datasets and can be faster than hash match for large, sorted tables.
Steps:
Sort Phase: If the tables are not already sorted, SQL Server sorts them.
Merge Phase: SQL Server scans both sorted tables and merges rows based on the join condition.
Advantages: Efficient for large, sorted datasets and uses less memory compared to hash match.
Disadvantages: Requires sorted input, which can add overhead if sorting is needed.
Summary
Hash Match: Best for large, unsorted datasets without suitable indexes. Memory-intensive but flexible.
Merge Join: Best for large, sorted datasets with suitable indexes. Efficient and less memory-intensive.
Choosing Between Them
SQL Server's query optimizer chooses the most appropriate join method based on factors like data size, indexes, and sorting. Understanding these differences can help you optimize your queries and interpret execution plans more effectively.
If you have more questions or need further clarification, feel free to ask!



When you have a VARCHAR column as a primary key (PK) and you insert rows in a non-ordered manner, SQL Server does not physically rearrange the entire table to keep the PK column ordered. Instead, it maintains the order logically through the use of indexes. Here’s how it works:

Clustered Index
Primary Key and Clustered Index: By default, the primary key constraint creates a clustered index on the column. A clustered index determines the physical order of data in the table.
Logical Order: The clustered index ensures that the data is logically ordered based on the primary key column. This means that SQL Server can quickly locate rows based on the PK, even if the data was inserted in a non-ordered manner.
Inserting Data
Non-Ordered Inserts: When you insert data that is not in order, SQL Server places the new rows in the appropriate position within the clustered index. This may involve splitting pages and reorganizing pointers, but it does not rearrange the entire table.
Page Splits: If a new row needs to be inserted into a full page, SQL Server performs a page split. It creates a new page and moves some of the rows to the new page to make room for the new row. This can cause fragmentation.
Performance Considerations
Fragmentation: Frequent non-ordered inserts can lead to fragmentation, which can degrade performance. You can monitor and manage fragmentation using tools like DBCC SHOWCONTIG and DBCC INDEXDEFRAG.
Fill Factor: You can set a fill factor for the index to leave some free space on each page, reducing the need for page splits.


ummary
SQL Server maintains the logical order of the primary key using a clustered index.
Non-ordered inserts do not rearrange the entire table but may cause page splits and fragmentation.
Managing fragmentation and setting an appropriate fill factor can help maintain performance.


Correct, while a primary key (PK) and a clustered index are related, they are not the same thing. Here’s a detailed explanation:

Primary Key (PK)
Definition: A primary key is a column or a set of columns that uniquely identifies each row in a table.
Uniqueness: Ensures that no duplicate values exist in the primary key column(s).
Not Null: Primary key columns cannot contain NULL values.
Constraint: When you define a primary key, SQL Server automatically creates a unique index on the column(s).
Clustered Index
Definition: A clustered index determines the physical order of data in the table. There can be only one clustered index per table because the data rows themselves are stored in the order of the clustered index.
Physical Order: The clustered index sorts and stores the data rows based on the index key.
Primary Key Relationship: By default, when you create a primary key, SQL Server creates a clustered index on the primary key column(s). However, you can specify a different index type if needed.
Differences
Purpose: The primary key is a logical construct that ensures uniqueness and non-nullability. The clustered index is a physical construct that determines the order of data storage.
Creation: A primary key automatically creates a unique index, which is usually clustered. However, you can create a primary key with a non-clustered index if desired.
Number: A table can have multiple unique indexes but only one clustered index.

Summary
Primary Key: Ensures uniqueness and non-nullability.
Clustered Index: Determines the physical order of data storage.
Relationship: A primary key usually creates a clustered index, but you can specify a non-clustered index if needed.


