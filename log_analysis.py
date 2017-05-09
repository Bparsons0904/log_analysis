# #!/usr/bin/env python3

import psycopg2

#views to be created
author_sum = """
create view author_sum as
  select slug, author, count(log.path) as sum
  from articles, log
  where log.path = '/article/' || articles.slug
  group by articles.author, articles.slug
  order by articles.author;"""

article_count = """
select slug, count(log.path) as sum
  from articles, log
  where log.path = '/article/' || articles.slug
  group by articles.slug
  order by sum desc limit 3;"""




DBNAME = "news"

def connect(create):
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute(create)
#  cursor.execute("select * from author_sum;")
#  results = cursor.fetchall()
#  return results
  conn.close()

def connect2(create):
  conn = psycopg2.connect(database=DBNAME)
  cursor = conn.cursor()
  cursor.execute(create)
  cursor.execute("select * from author_sum;")
  results = cursor.fetchall()
  return results
  conn.close()

print(connect(author_sum))
#print(connect2(author_sum))

#print connect()
#print(connect)("select * from author_sum")


# python3 log_analysis.py
# psql -d news
# select * from author_sum;

#  return c.fetchall()
