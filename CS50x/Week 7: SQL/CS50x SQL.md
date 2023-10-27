# SQL
SQL is a [[ST Query Language]] used to insert, retrieve and manipulate data in [[CS50x Relational Databases]]

## Syntax
- A database is manipulated with SQL through *queries*  
    - Each query has one or more *statements*
        - Each statement has
            - Clauses
            - Expressions
            - Predicates
            - Literals

### Clauses
A clause is an action to be performed with the data, or a conditional
- `SELECT`: Retrieves data
- `INSERT`: Inserts a new row on the specified columns with the given `VALUES`
- `VALUES`: Specifies the values to be inserted
- `WHERE`: Creates the condition of *where* to perform the action (e.g where to retrieve data from)
- `UPDATE`: Overwrites data in a table, used with `SET`
- `SET`: Specifies what data to overwrite from a table given by `UPDATE`
....

### Expressions
Expressions produce values or tables, depending on what clause was used before the expression


```sql
UPDATE countries SET population = population + 1 WHERE name = 'USA';
```

On the above codeblock `population + 1` is an expression, which will produce a number. `USA` is also an expression, along with `WHERE` it generates a table where `SET` will act upon

### Predicates
Predicates are condition which, along with expressions, limit where the Clauses will act upon

