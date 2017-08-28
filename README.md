# Logs Analysis Project
##### The project for Udacity quiz - "Logs Analysis Project"

In this project complex SQL queries are used for generating the reports. These are the following technologies: 
- database: PostgreSQL
- language: Python v3.6.1

## Installation
For installation you have to have: 
- installed Python 3.5 version or more
- installed PostgreSQL 9.6
- uploaded in to PostgreSQL - [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

#### Preparation
In PostgreSQL create following VIEWS:
```
CREATE OR REPLACE VIEW public.top_articles AS 
 SELECT log.path,
    count(log.path) AS amount
   FROM log
  WHERE log.path ~~ '%/article/%'::text
  GROUP BY log.path
  ORDER BY (count(log.path)) DESC;

ALTER TABLE public.top_articles
  OWNER TO postgres;
```
```
CREATE OR REPLACE VIEW public.request_list AS 
 SELECT date(log."time") AS day,
    count(log.status)::double precision AS requests
   FROM log
  GROUP BY (date(log."time"))
  ORDER BY (count(log.status)::double precision) DESC;

ALTER TABLE public.request_list
  OWNER TO postgres;
```
```
CREATE OR REPLACE VIEW public.error_list AS 
 SELECT date(log."time") AS day,
    count(log.status)::double precision AS errors
   FROM log
  WHERE log.status <> '200 OK'::text
  GROUP BY (date(log."time"))
  ORDER BY (count(log.status)::double precision) DESC;

ALTER TABLE public.error_list
  OWNER TO postgres;
```
> In file main.py change SETTINGS['db'] on your database name
#### Installation with git
In Git Bash put the following command:
```
git clone "https://github.com/DudkinON/log_analytic"
```
```
pip install psycopg2
```
```
python log_analytic/main.py
```


