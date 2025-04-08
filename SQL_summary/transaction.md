# SQL Transactions


In SQL Server, you can find tables containing a specific column name using the INFORMATION_SCHEMA.COLUMNS view or 
the sys.columns and sys.tables system views. Here's how to do it using both methods:

1. Using INFORMATION_SCHEMA.COLUMNS:

This is generally the more portable method across different SQL Server versions.

SQL

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    COLUMN_NAME = 'YourColumnName'; -- Replace 'YourColumnName' with the actual column name you're searching for
Explanation:

INFORMATION_SCHEMA.COLUMNS: This view provides information about columns in tables and views.
TABLE_SCHEMA: The schema of the table.
TABLE_NAME: The name of the table.
COLUMN_NAME: The name of the column.
The WHERE clause filters the results to include only rows where the COLUMN_NAME matches the specified name.
Example:

To find tables containing the column CustomerID, you would run:

SQL

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    COLUMN_NAME = 'CustomerID';
2. Using sys.columns and sys.tables:

This method uses system views and can be more efficient in some cases, but it's specific to SQL Server.

SQL

SELECT
    s.name AS SchemaName,
    t.name AS TableName
FROM
    sys.columns c
JOIN
    sys.tables t ON c.object_id = t.object_id
JOIN
    sys.schemas s ON t.schema_id = s.schema_id
WHERE
    c.name = 'YourColumnName'; -- Replace 'YourColumnName' with the actual column name
Explanation:

sys.columns: This view contains information about columns.
sys.tables: This view contains information about tables.
sys.schemas: This view contains information about schemas.
c.object_id = t.object_id: This joins the sys.columns and sys.tables views based on the object ID, which is the common identifier for tables and columns.
t.schema_id = s.schema_id: This joins the sys.tables and sys.schemas views to get the schema name.
c.name = 'YourColumnName': This filters the results to include only rows where the column name matches the specified name.
Example:

To find tables containing the column ProductName, you would run:

SQL

SELECT
    s.name AS SchemaName,
    t.name AS TableName
FROM
    sys.columns c
JOIN
    sys.tables t ON c.object_id = t.object_id
JOIN
    sys.schemas s ON t.schema_id = s.schema_id
WHERE
    c.name = 'ProductName';
Important Considerations:

Case Sensitivity: Column names are generally case-insensitive in SQL Server by default, but this can depend on the collation of your database. If you need case-sensitive searching, adjust the WHERE clause accordingly.   
Wildcards: If you want to find columns with names that contain a specific pattern, you can use the LIKE operator with wildcards (% for any sequence of characters, _ for a single character). For example, to find columns containing "ID" anywhere in their name:
SQL

SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    COLUMN_NAME LIKE '%ID%';
Choose the method that best suits your needs and coding style. The INFORMATION_SCHEMA method is more portable, while the sys views can offer better performance in some scenarios.





I have INT PK, how do i know it is auto increment or not?


When dealing with SQL Server, determining if an INT primary key (PK) is auto-incrementing involves checking for the IDENTITY property. Here's a breakdown of how to do that:

Understanding IDENTITY

In SQL Server, the IDENTITY property is what designates a column as auto-incrementing.
It automatically generates sequential numeric values when new rows are inserted into a table.
How to Check

You can use the sys.columns system view to determine if a column has the IDENTITY property. Here's the SQL query:

SQL

SELECT
    OBJECT_NAME(c.object_id) AS TableName,
    c.name AS ColumnName,
    c.is_identity
FROM
    sys.columns c
WHERE
    c.object_id = OBJECT_ID('YourTableName') -- Replace 'YourTableName'
    AND c.name = 'YourColumnName'; -- Replace 'YourColumnName'
Explanation:

sys.columns: This system view contains information about columns in database tables.
OBJECT_NAME(c.object_id): this returns the table name that the object_id relates to.
c.name: this returns the column name.
c.is_identity: This column returns 1 if the column has the IDENTITY property, and 0 otherwise.
OBJECT_ID('YourTableName'): This function gets the object ID of the specified table.
The WHERE clause filters the results to the specific table and column you're interested in.
Example

If you want to check if the CustomerID column in the Customers table is auto-incrementing, you would use:

SQL

SELECT
    OBJECT_NAME(c.object_id) AS TableName,
    c.name AS ColumnName,
    c.is_identity
FROM
    sys.columns c
WHERE
    c.object_id = OBJECT_ID('Customers')
    AND c.name = 'CustomerID';
Key Points:

If the is_identity column in the result is 1, the column is auto-incrementing.
If it's 0, the column is not auto-incrementing.
Remember to replace 'YourTableName' and 'YourColumnName' with the actual table and column names.
By using this method, you can reliably determine whether an INT primary key is configured for auto-incrementing in your SQL Server database.





the column fullName looks like LastName +', ' + FirstName. How can I get LastName and FirstName from the fullName in sql query


You can extract LastName and FirstName from the fullName column using string manipulation functions in SQL Server, specifically CHARINDEX, LEFT, and RIGHT. Here's how you can do it:

SQL Query:

SQL

SELECT
    fullName,
    LEFT(fullName, CHARINDEX(',', fullName) - 1) AS LastName,
    RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1) AS FirstName
FROM
    YourTableName; -- Replace 'YourTableName' with the actual table name
Explanation:

CHARINDEX(',', fullName):
This finds the position of the comma (,) within the fullName string.
LEFT(fullName, CHARINDEX(',', fullName) - 1):
This extracts the LastName.
LEFT returns a specified number of characters from the left side of a string.
We use CHARINDEX(',', fullName) - 1 to get the length of the LastName (up to the comma).
RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1):
This extracts the FirstName.
Right returns a specified number of characters from the right side of a string.
LEN(fullName) gets the total length of the full name.
CHARINDEX(',', fullName) + 1 gets the starting position of the first name.
We subtract the starting position of the first name from the total length of the full name, to get the length of the first name.
YourTableName:
Replace this with the actual name of your table.
Example:

If you have a table named Employees with a fullName column, and you want to extract LastName and FirstName, you would use:

SQL

SELECT
    fullName,
    LEFT(fullName, CHARINDEX(',', fullName) - 1) AS LastName,
    RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1) AS FirstName
FROM
    Employees;
Important Notes:

Error Handling:
This query assumes that all fullName values are in the format "LastName, FirstName". If there are any variations (e.g., missing commas, extra spaces), the query might produce unexpected results or errors.
If some fullnames do not have a comma, the query will produce errors. You can add a where clause to only process rows that have a comma.
You can use ISNULL or CASE statements to handle potential errors or variations in the data.
Spaces:
If there are extra spaces around the comma or the names, you might need to use the TRIM function to remove them. For example:
SQL

SELECT
    fullName,
    TRIM(LEFT(fullName, CHARINDEX(',', fullName) - 1)) AS LastName,
    TRIM(RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1)) AS FirstName
FROM YourTableName;
Performance:
String manipulation can be computationally expensive, especially on large tables. If performance is a concern, consider optimizing the query or pre-processing the data.




if there is no ',' then I want to set LastName and FirstName as null


You can handle cases where the fullName column doesn't contain a comma by using a CASE statement to check for the presence of the comma before attempting to extract the LastName and FirstName. Here's the modified SQL query:

SQL

SELECT
    fullName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN LEFT(fullName, CHARINDEX(',', fullName) - 1)
        ELSE NULL
    END AS LastName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1)
        ELSE NULL
    END AS FirstName
FROM
    YourTableName; -- Replace 'YourTableName' with the actual table name
Explanation:

CASE WHEN CHARINDEX(',', fullName) > 0 THEN ... ELSE NULL END:
This CASE statement checks if the CHARINDEX(',', fullName) is greater than 0, which means a comma was found in the fullName.
If a comma is found, it proceeds with the LEFT or RIGHT extraction as before.
If no comma is found (i.e., CHARINDEX(',', fullName) is 0), it returns NULL for both LastName and FirstName.
Example:

If you have a table named Employees and you want to handle cases where the fullName column might not have a comma, you would use:

SQL

SELECT
    fullName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN LEFT(fullName, CHARINDEX(',', fullName) - 1)
        ELSE NULL
    END AS LastName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1)
        ELSE NULL
    END AS FirstName
FROM
    Employees;
Handling Extra Spaces (Optional):

If you also want to trim any extra spaces around the extracted names, you can combine the TRIM function with the CASE statement:

SQL

SELECT
    fullName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN TRIM(LEFT(fullName, CHARINDEX(',', fullName) - 1))
        ELSE NULL
    END AS LastName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN TRIM(RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1))
        ELSE NULL
    END AS FirstName
FROM
    YourTableName;
By using the CASE statement, you can ensure that your query handles cases where the fullName column doesn't conform to the expected "LastName, FirstName" format without causing errors.





'TRIM' is not a recognized built-in function name.


You are absolutely correct! My apologies. The TRIM function was introduced in SQL Server 2017 (version 14.x). If you're using an older version of SQL Server, you'll need to use LTRIM and RTRIM to achieve the same result.

Here's the corrected SQL query that will work in older SQL Server versions:

SQL

SELECT
    fullName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RTRIM(LTRIM(LEFT(fullName, CHARINDEX(',', fullName) - 1)))
        ELSE NULL
    END AS LastName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RTRIM(LTRIM(RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1)))
        ELSE NULL
    END AS FirstName
FROM
    YourTableName; -- Replace 'YourTableName' with the actual table name
Explanation of LTRIM and RTRIM:

LTRIM(string): Removes leading spaces from a string.
RTRIM(string): Removes trailing spaces from a string.
How the Correction Works:

We apply both LTRIM and RTRIM to the extracted LastName and FirstName to remove any leading or trailing spaces. This ensures that the results are clean, even if there were extra spaces around the comma or the names.
Example:

SQL

SELECT
    fullName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RTRIM(LTRIM(LEFT(fullName, CHARINDEX(',', fullName) - 1)))
        ELSE NULL
    END AS LastName,
    CASE
        WHEN CHARINDEX(',', fullName) > 0 THEN RTRIM(LTRIM(RIGHT(fullName, LEN(fullName) - CHARINDEX(',', fullName) - 1)))
        ELSE NULL
    END AS FirstName
FROM
    Employees;
Again, my sincere apologies for the error. Thank you for pointing it out!





col1 has value like 000116_48116 or _1560 hwo to get the number or text after "_". If no underscore set null


You can extract the number or text after the underscore (_) in col1 using CHARINDEX, SUBSTRING, and a CASE statement to handle cases where there's no underscore. Here's the SQL query:

SQL

SELECT
    col1,
    CASE
        WHEN CHARINDEX('_', col1) > 0 THEN SUBSTRING(col1, CHARINDEX('_', col1) + 1, LEN(col1))
        ELSE NULL
    END AS extracted_value
FROM
    YourTableName; -- Replace 'YourTableName' with the actual table name
Explanation:

CHARINDEX('_', col1):
This finds the position of the underscore in col1.
CASE WHEN CHARINDEX('_', col1) > 0 THEN ... ELSE NULL END:
This CASE statement checks if an underscore exists in col1.
If an underscore exists (i.e., CHARINDEX('_', col1) > 0), it proceeds to extract the value after the underscore.
If no underscore exists, it returns NULL.
SUBSTRING(col1, CHARINDEX('_', col1) + 1, LEN(col1)):
SUBSTRING extracts a part of a string.
CHARINDEX('_', col1) + 1 is the starting position of the substring (the character after the underscore).
LEN(col1) is the length of the entire string, which effectively extracts everything from the character after the underscore to the end of the string.
Example:

If you have a table named Data with a column col1, you would use:

SQL

SELECT
    col1,
    CASE
        WHEN CHARINDEX('_', col1) > 0 THEN SUBSTRING(col1, CHARINDEX('_', col1) + 1, LEN(col1))
        ELSE NULL
    END AS extracted_value
FROM
    Data;
Handling Potential Issues:

Leading/Trailing Spaces: If the extracted value might have leading or trailing spaces, you can add LTRIM and RTRIM (or TRIM in SQL Server 2017+) to clean it up:
SQL

SELECT
    col1,
    CASE
        WHEN CHARINDEX('_', col1) > 0 THEN RTRIM(LTRIM(SUBSTRING(col1, CHARINDEX('_', col1) + 1, LEN(col1))))
        ELSE NULL
    END AS extracted_value
FROM
    YourTableName;
Multiple Underscores: If col1 might contain multiple underscores, this query will extract the value after the first underscore. If you need different behavior, you'll need to adjust the logic accordingly.




alter table add column?


In SQL Server, you use the ALTER TABLE statement with the ADD clause to add a new column to an existing table. Here's a breakdown of the syntax and important considerations:

Basic Syntax:

SQL

ALTER TABLE table_name
ADD column_name data_type [constraints];
Explanation:

ALTER TABLE table_name: Specifies the table you want to modify.
ADD column_name data_type: Defines the name of the new column and its data type (e.g., INT, VARCHAR, DATE).
[constraints]: Optional constraints, such as NULL, NOT NULL, DEFAULT, or CHECK, that define rules for the column's data.
Examples:

Adding a simple column:

SQL

ALTER TABLE Employees
ADD Department VARCHAR(50);
This adds a Department column of type VARCHAR(50) to the Employees table. By default, this column will allow NULL values.

Adding a column with a NOT NULL constraint:

SQL

ALTER TABLE Customers
ADD Email VARCHAR(100) NOT NULL;
This adds an Email column that cannot contain NULL values.

Adding a column with a DEFAULT constraint:

SQL

ALTER TABLE Orders
ADD OrderDate DATE DEFAULT GETDATE();
This adds an OrderDate column with a default value of the current date and time.

Important Considerations:

Data Type:
Choose the appropriate data type for the column based on the type of data it will store.
NULLability:
Decide whether the column should allow NULL values.
If you use NOT NULL, you might need to provide default values or update existing rows to populate the new column.
Constraints:
Use constraints to enforce data integrity and business rules.
Performance:
Adding a column to a large table can impact performance, especially if the NOT NULL constraint is used.
It's often recommended to perform such operations during off-peak hours.
Existing Data:
When you add a column, existing rows will have NULL values in that column unless you specify a DEFAULT constraint or update the rows.
Multiple Columns:
You can add multiple columns in one ALTER TABLE statement. For example:
SQL

ALTER TABLE MyTable
ADD Column1 INT,
ADD Column2 VARCHAR(50);
I hope this helps!





I have a sql server agent job which get data from a linked server and insert target table with non-duplicated records. But around OS patching, It inserts some duplicated records. how to handle this? what cause this problem. During regular time it works fine.



The issue of duplicated records appearing in your SQL Server Agent job's target table after OS patching is a classic symptom of concurrency and transaction management problems, likely exacerbated by the patching process. Here's a breakdown of the probable causes and how to handle them:

Probable Causes:

Linked Server Instability During Patching:
OS patching can temporarily disrupt network connectivity or linked server availability. If your SQL Server Agent job runs during this window, it might experience partial failures or retries, leading to duplicate data.
The linked server might temporarily go offline or become unresponsive, and the SQL Server Agent job's logic might not properly handle these transient errors.
Transaction Isolation Levels:
If your job's logic involves reading from the linked server and then inserting into the target table, the transaction isolation level can play a significant role.
If the isolation level is too permissive (e.g., READ UNCOMMITTED), it might read data that is still being modified on the linked server, leading to inconsistencies.
During patching, the linked server might experience temporary data inconsistencies, which are then read by your job.
Job Retries and Error Handling:
If your SQL Server Agent job has retry logic, and the job fails during patching, it might retry the insertion process multiple times, resulting in duplicates.
Insufficient error handling in the job's T-SQL code might not properly prevent duplicate insertions during retries.
Concurrency Issues:
If other processes are also inserting or modifying data in the target table or the linked server during patching, it can lead to concurrency conflicts.
Locks that are held for longer than usual due to the OS patching, can cause time outs, and job retries.
Linked server time outs:
OS patching can cause network latency, or linked server performance degradation. This can cause time outs on the linked server query, which can cause the job to rerun, and cause duplicates.
How to Handle the Problem:

Robust Error Handling and Transaction Management:
Implement explicit transactions in your SQL Server Agent job's T-SQL code.
Use TRY...CATCH blocks to handle potential errors gracefully.
Implement proper logging to track job execution and errors.
If the Linked server is unavailable, add a delay, and retry the connection.
Improved Job Logic:
Instead of simply inserting all data from the linked server, use a MERGE statement to insert or update records based on a unique key.
This will prevent duplicates by updating existing records instead of creating new ones.
Implement a staging table to temporarily store data from the linked server. Then, perform the deduplication and insertion into the target table in a separate step.
Adjust Transaction Isolation Levels:
Use a more restrictive transaction isolation level, such as READ COMMITTED or SERIALIZABLE, to prevent reading inconsistent data.
Job Scheduling:
If possible, schedule the SQL Server Agent job to run outside of the OS patching window.
Linked Server Timeout and Retry Logic:
Increase the linked server timeout value.
Implement retry logic, with exponential backoff, within the SQL job, when linked server queries fail.
Unique Constraints/Indexes:
Ensure that the target table has a unique constraint or index on the columns that should prevent duplicates.
This will enforce data integrity at the database level.
Logging:
Add extensive logging to the sql agent job. This will allow you to see exactly what happened during the OS patching window. Log the linked server connections, the queries run, and the rows inserted.
Example MERGE Statement:

SQL

MERGE TargetTable AS target
USING (SELECT * FROM LinkedServer.Database.Schema.SourceTable) AS source
ON target.UniqueKey = source.UniqueKey
WHEN MATCHED THEN
    -- Update existing records
    UPDATE SET target.Column1 = source.Column1, target.Column2 = source.Column2
WHEN NOT MATCHED THEN
    -- Insert new records
    INSERT (UniqueKey, Column1, Column2)
    VALUES (source.UniqueKey, source.Column1, source.Column2);
By implementing these strategies, you can improve the robustness of your SQL Server Agent job and minimize the risk of duplicate data insertions, even during OS patching.





how to use try catch and transaction in sql server. give me some example. where should i put logging logic.


Using TRY...CATCH blocks and transactions in SQL Server is essential for robust error handling and data integrity. Here's a detailed example with logging logic:

Example Scenario:

Imagine you have a stored procedure that inserts data into a table based on data retrieved from a linked server. You want to ensure that if any part of the process fails, the entire operation is rolled back, and you want to log any errors that occur.

SQL Code:

SQL

CREATE PROCEDURE InsertDataFromLinkedServer
AS
BEGIN
    SET NOCOUNT ON; -- Prevents row count messages

    DECLARE @TranCount INT;
    DECLARE @ErrorMessage NVARCHAR(MAX);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    SET @TranCount = @@TRANCOUNT;

    IF @TranCount = 0
        BEGIN TRANSACTION;
    ELSE
        SAVE TRANSACTION InsertDataTransaction;

    BEGIN TRY
        -- 1. Get data from linked server
        INSERT INTO TargetTable (Column1, Column2)
        SELECT Column1, Column2
        FROM LinkedServer.Database.Schema.SourceTable;

        -- 2. Some other operations
        UPDATE TargetTable SET Column1 = 'Updated' WHERE Column2 = 'SomeValue';

        -- 3. If all operations are successful, commit transaction
        IF @TranCount = 0
            COMMIT TRANSACTION;
        ELSE
            COMMIT TRANSACTION InsertDataTransaction;

        -- Log success
        INSERT INTO LogTable (LogMessage, LogDateTime)
        VALUES ('Data inserted successfully.', GETDATE());
    END TRY
    BEGIN CATCH
        -- Get error information
        SET @ErrorMessage = ERROR_MESSAGE();
        SET @ErrorSeverity = ERROR_SEVERITY();
        SET @ErrorState = ERROR_STATE();

        -- Rollback transaction
        IF @TranCount = 0
            ROLLBACK TRANSACTION;
        ELSE
            IF XACT_STATE() <> -1
                ROLLBACK TRANSACTION InsertDataTransaction;

        -- Log error
        INSERT INTO LogTable (LogMessage, LogDateTime, ErrorSeverity, ErrorState)
        VALUES (@ErrorMessage, GETDATE(), @ErrorSeverity, @ErrorState);

        -- Rethrow error (optional, for calling applications)
        RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH;
END;
Explanation:

Transaction Management:
@@TRANCOUNT: Keeps track of the number of active transactions.
BEGIN TRANSACTION: Starts a new transaction if no transaction is already active.
SAVE TRANSACTION InsertDataTransaction: Creates a savepoint if a transaction is already active.
COMMIT TRANSACTION: Commits the transaction if all operations are successful.
ROLLBACK TRANSACTION: Rolls back the transaction if any error occurs.
XACT_STATE(): Checks the state of the current transaction. This is important to ensure that we only rollback if the transaction is still active.
TRY...CATCH Block:
The TRY block contains the code that might cause an error.
The CATCH block handles any errors that occur within the TRY block.
Error Handling:
ERROR_MESSAGE(), ERROR_SEVERITY(), and ERROR_STATE(): Retrieve information about the error.
RAISERROR: Rethrows the error, which allows calling applications to handle it.
Logging:
LogTable: A table to store log messages, timestamps, and error details.
Logging is done inside both the TRY and CATCH blocks.
Logging within the TRY block lets you know the process was successful.
Logging within the CATCH block provides detailed information about errors.
Where to Put Logging Logic:

Inside the TRY Block:
Log successful operations to track the flow of the process.
Log key events or milestones.
Inside the CATCH Block:
Log error messages, severity, and state.
Log the values of relevant variables or parameters.
Log the timestamp of the error.
Before and After Transactions:
Log the start and end of transactions.
Log any changes to transaction state.
Linked server connections:
Log when the linked server connection is established, and when it is closed. Log any errors that occur when trying to connect to the linked server.
Queries:
Log the queries that are being executed against the linked server.
Row Counts:
Log the number of rows that are being inserted, updated, or deleted.
Key Considerations:

LogTable Design: Design your LogTable to store relevant information for debugging and auditing.
Error Detail: The more detail you log, the easier it will be to diagnose problems.
Performance: Excessive logging can impact performance. Consider logging only essential information.
Security: Be mindful of logging sensitive data.
Transaction Scope: Understand the scope of your transactions and ensure that all related operations are included within the transaction boundaries.
SET XACT_ABORT ON: Consider using SET XACT_ABORT ON at the start of your stored procedure. This will cause the entire transaction to be rolled back if any runtime error occurs.
By using TRY...CATCH blocks, transactions, and appropriate logging, you can create robust and reliable SQL Server code.





what is  @@TRANCOUNT?


In SQL Server, @@TRANCOUNT is a system function that returns the number of active BEGIN TRANSACTION statements for the current connection. Essentially, it keeps track of the nesting level of transactions.

Here's a breakdown:

Purpose:
It's used to manage nested transactions and to determine whether a transaction is currently active.   
How it Works:
BEGIN TRANSACTION increments @@TRANCOUNT by 1.
COMMIT TRANSACTION decrements @@TRANCOUNT by 1.
ROLLBACK TRANSACTION (without a savepoint name) sets @@TRANCOUNT to 0, effectively ending all active transactions.
ROLLBACK TRANSACTION savepoint_name does not affect the value of @@TRANCOUNT.
Usage:
It's particularly useful in stored procedures or complex scripts where you might have nested transactions.
By checking @@TRANCOUNT, you can ensure that you commit or roll back transactions correctly.
It is very useful when dealing with nested transactions, and when trying to make sure that a rollback, only rolls back the correct amount of the transaction.
In simpler terms, @@TRANCOUNT tells you how many "open transaction layers" you have. If it's 0, there are no active transactions. If it's greater than 0, there are one or more active transactions.   


Sources and related content
@@TRANCOUNT and savepoints | SQL - DataCamp

campus.datacamp.com






IF @TranCount = 0

ROLLBACK TRANSACTION;

ELSE

IF XACT_STATE() <> -1

ROLLBACK TRANSACTION InsertDataTransaction;

why do need the other condition IF XACT_STATE() <> -1?



You're right to question that! The IF XACT_STATE() <> -1 condition in the ELSE part of the ROLLBACK TRANSACTION logic is crucial for robust transaction handling, especially in nested transactions. Here's why:

Understanding XACT_STATE():

XACT_STATE() is a SQL Server function that returns the state of the current user transaction. It can return one of three values:
1: The transaction is active and committable.
0: There is no active transaction.
-1: The transaction is active but uncommittable (i.e., it has been marked for rollback).
Why IF XACT_STATE() <> -1 is Important:

Handling Uncommittable Transactions:
If an error occurs within a nested transaction, the entire transaction might be marked as uncommittable (XACT_STATE() = -1).
In this state, attempting to COMMIT TRANSACTION will result in an error.
Similarly, attempting to ROLLBACK TRANSACTION savepoint_name when the transaction is already in an uncommittable state can also lead to issues.
Preventing Double Rollbacks:
If the transaction is already in an uncommittable state, it means that a rollback has already been implicitly requested by SQL Server.
Executing another ROLLBACK TRANSACTION in this situation can cause unexpected behavior or errors.
By checking that XACT_STATE() is not equal to -1, you are making sure that you only attempt to rollback the save point, if the transaction is still in a valid state.
Ensuring Correct Rollback Behavior:
By adding that condition, you guarantee that if the transaction is already in a state of being rolled back, you do not try to roll back the save point. This ensures that the transaction is only rolled back once.
Nested Transaction Scenarios:
In nested transactions, you might have multiple savepoints.
If an error occurs in an inner transaction, you might want to roll back to a specific savepoint.
However, if the outer transaction has already been marked as uncommittable, attempting to roll back to an inner savepoint might not be the desired behavior.
In essence, the IF XACT_STATE() <> -1 condition acts as a safety measure to prevent errors and ensure that rollbacks are performed correctly, especially in complex transaction scenarios.

Therefore, the complete logic:

SQL

IF @TranCount = 0
    ROLLBACK TRANSACTION;
ELSE
    IF XACT_STATE() <> -1
        ROLLBACK TRANSACTION InsertDataTransaction;
Ensures that if it is the outter most transaction, then it is rolled back fully, but if it is a nested transaction, it only rolls back to the save point, if the transaction is still in a valid state.