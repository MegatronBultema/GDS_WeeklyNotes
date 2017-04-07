Notes on SQL
Here are the different types of the JOINs in SQL:

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Return all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Return all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Return all records when there is a match in either left or right table

https://www.w3schools.com/sql/sql_join.asp

Frank - first thing I do is pull out of SQL into pandas but interview and jobs want SQL
ERD show common columns

Postgres not equal <>
sqlzoo not equal !=

SQL is focused on what results you want to gain
Python is focused on how to do a activity
SELECT UNIQUE - gives unique combinations of the selection
WHERE - does not recognize aliases, can reference a column that is not in select
    can you AND (both need to be true) OR
operators - ^ is used for exponents, can add columns in select
divide by int you get int, operate by float you get float

CASE WHEN ___ THEN __
    ELSE __ END

aggregators - combine information from multiple rows
COUNT(* ) gives total number of rows

any column that is not an aggregator must be in the group by (in effect it aggregates it)
or you can have multiple columns that are aggregated

Any column in the group by clause must also appear in the select clause

WHERE doesn't recognize aggregates
HAVING allows you to filter using an aggregator

PK should be UNIQUE
FK uniquely identify PK in other tables
Check launch that psql is turned on


 REFERENCES student (id) - gives foriegn key
 numeric(3,2) --- 3 numbers 2 decimal
 choice characters over text types
 
