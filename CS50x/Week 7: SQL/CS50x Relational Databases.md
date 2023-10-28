# Relational Databases
A relational database is a [[CS50x Databases]], usually implemented in [[CS50x SQL]], with multiple tables (sometimes refered as *relations*) which allows linking of values between tables to form other tables with specific relationships

## Relationships
Each record in a table has a unique identifier field. This prevent us from adding fields that can have multiple values for the same entity

### Example
Given a table of Movies
| id  | title  | year  | 
|-----| ------ | ----- |
|1234 |  Star Wars IV: The Empire Strikes Back| 1977

Each value in that table is unique. A movie can't have two titles or two release dates
But a movie can have more than one genre. In this case `space opera`, `sci-fi` and `adventure`, but to include those we'd need to have the same movie in multiple rows. That approach isn't good since the movie has a unique identifier, which would change in the following rows

To solve that we can build a second table *genres*, where each row has: 
- An ID that references a movie in the first table
- The genre of that movie

The id comes from the first table, and it is repeated in the following rows in case the same movie appears more than once

| movie_id| genre      |
|-------- | -----------|
| 1234    | sci-fi     |
| 1234    | space opera|
| 1234    | adventure  |

`movie_id` can be used to search the first table and get other details about the movie

The original id in the first table is called a **Primary ID**, and its reference in the second table is a **Foreign ID**

The details of a movie can be retrieved by its genre through the following *SQL query*
```sql
SELECT * FROM Movies WHERE id IN (SELECT movie_id FROM Genres = 'sci-fi')
```
This will retrieve all shows with the genre sci-fi present in the first table.
A similar result is possible with the keyword `JOIN`

```sql
SELECT * FROM Movies JOIN Genres ON movies.id = Genres.show_id
```

It literally joins the two tables, giving the rows that have equal ids in both tables

| id |    title     | year | movie_id | genre  |
|----|--------------|------|----------|--------|
| 1  | Star Wars IV | 1977 | 1        | sci-fi |



