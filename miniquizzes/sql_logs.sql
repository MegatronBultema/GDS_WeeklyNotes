

CREATE DATABASE retail_log;
CREATE TABLE log (
    userid   int,
    tmstmp   timestamp,
    itemid   int,
    event    varchar(10));

COPY log FROM '/Users/DataScience/Documents/GDS_WeeklyNotes/miniquizzes' CSV;

SELECT * FROM log;
/*SELECT * FROM log WHERE event = 'buy';*/

CREATE TEMPORARY TABLE buy_log as (SELECT * FROM log WHERE event = 'buy')

CREATE TEMPORARY TABLE add_log as (SELECT * FROM log WHERE event = 'add')

SELECT t1.*
FROM add_log as t1
LEFT JOIN buy_log as t2 ON t2.userid = t1.userid and t2.itemid = t1.itemid
WHERE t2.userid IS NULL

;

/* In the terminal run
psql -f sql_logs.sql retail_log
*/
