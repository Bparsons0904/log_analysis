Steps to run program:
  1. Use scripts below to create 4 (author_sum, author_name, error and success) views.
  2. Run python3 log_anaylsis.py

view: Count of articles w/ author ID

create view author_sum as
  select slug, author, count(log.path)::numeric as sum
  from articles, log
  where log.path = '/article/' || articles.slug
  group by articles.author, articles.slug
  order by articles.author;

  | Column | Type   |
  | :------| :----- |
  | slug   | text   |
  | sum    | bigint |


author_name view: Link author ID to real name.

create view author_name as
  select authors.name, articles.slug
  from authors, articles
  where authors.id=articles.author
  group by authors.name, articles.slug;

  | Column | Type   |
  | :------| :----- |
  | name   | text   |
  | slug   | text   |


error view: Count days with errors in the connections

create view error as
  select date(time), count(*) as errors
  from log
  where status not like '200%'
  group by date(time)
  order by date(time);

  | Column      | Type             |
  | :-----------| :--------------- |
  | date_part   | double precision |
  | errors      | bigint           |


success view: Count days with errors in the connections

create view success as
  select date(time), count(*) as success
  from log
  where status like '200%'
  group by date(time)
  order by date(time);

  | Column      | Type             |
  | :-----------| :--------------- |
  | date_part   | double precision |
  | success     | bigint           |
