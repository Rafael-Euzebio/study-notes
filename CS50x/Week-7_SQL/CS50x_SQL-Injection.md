# SQL Injection
SQL Injection is an attack which injects [SQL](./CS50x_SQL.md) Queries from a entry field to be executed on the server side

It consists of inserting SQL Queries and take advantage of SQL Statements that are executed on the server, possibly making changes to the database, ignoring part of the original SQL statement to get unauthorized access or even destroying the whole database

## Example
```sql
txtUserId = getRequestString("UserId");
"SELECT UserId, Name, Password FROM Users WHERE UserId = " + txtUserId;
```

The above SQL statement retrieves the UserId, Name and Password from the row that has the specified `txtUserId`  
Supposing `txtUserId` came from a user input (like an online form), the user could try to guess that the server appends any input to SQL statements and insert:

```sql
105 OR 1=1
```
The SQL statement would become

```sql
SELECT UserId, Name, Password FROM Users WHERE UserId = 105 OR 1=1
```
The above statement returns **all** rows from the database because `1=1` is always *True*  
or even insert:

```sql
SELECT UserId, Name, Password FROM Users WHERE UserId = 105; DROP TABLE Suppliers
```
Which would destroy all data inside the Suppliers table
