author_sum view: Count of articles w/ author ID

create view author_sum as
  select slug, author, count(log.path) as sum
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
  select extract(day from time), count(*) as errors
  from log
  where status not like '200%'
  group by extract(day from time)
  order by extract(day from time);

  | Column      | Type             |
  | :-----------| :--------------- |
  | date_part   | double precision |
  | errors      | bigint           |


success view: Count days with errors in the connections

create view success as
  select extract(day from time), count(*) as success
  from log
  where status like '200%'
  group by extract(day from time)
  order by extract(day from time);

  | Column      | Type             |
  | :-----------| :--------------- |
  | date_part   | double precision |
  | success     | bigint           |
