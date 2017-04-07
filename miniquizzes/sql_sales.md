## 1. SQL

Assume we have a table called `sales` with the following schema:

|user_id | item_id | price | source |
|:--:| :--:|:--:|:--:|
| 2 | 45 | 25 | in_store |
| 567 | 5 | 12 | online |
| 57 | 200 | 9 | affiliate |
| 10 | 7 | 703 | online |
| ... | ... | ... | ... |

1. Write a SQL query that returns total amount of revenue from the affiliate network.

  SELECT SUM(price) as revenue
  FROM sales
  WHERE source = 'affiliate';

2. Write a SQL query that returns total amount of revenue from each source.

  SELECT SUM(price) as revenue
  FROM sales
  GROUP BY source;

## 2. Joins

What is the resulting table of...
1. An inner join -

Returns records that have matching values in both tables

  department_id

2. A left outer join-

Return all records from the left table, and the matched records from the right table

  | employee_id | department_id | name | salary | and department_id from 2nd table

3. A full outer join-

Return all records when there is a match in either left or right table

All catagories all records

| employee_id | department_id | name | salary |
|:--:|:--:|:--:|:--:|
| 2 | 1 | Jon | 40000 |
| 7 | 1 | Linda | 50000 |
| 12 | 2 | Ashley | 15000 |
| 1 | 0 | Mike | 80000 |

and
department_id	location
1	NY
2	SF
3	Austin
