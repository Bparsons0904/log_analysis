#!/usr/bin/env python3

import psycopg2

# scripts for questions 1-3

# Counts total articles and outputs top 3 results. Q1
question1 = """
select slug, count(log.path) as sum
  from articles, log
  where log.path = '/article/' || articles.slug
  group by articles.slug
  order by sum desc limit 3;"""
# Counts total articles by author and outputs top 3 results. Q2
question2 = """
select author_name.name, sum(author_sum.sum) as total
  from author_name, author_sum
  where author_sum.slug=author_name.slug
  group by author_name.name
  order by total desc limit 3;"""
# Compared error rate by date, outputing days over 1%
question3 = """
select error.date_part, error.errors, success.success
  from error, success
  where error.date_part=success.date_part and error.errors/success.success::float > .01
  group by error.date_part, error.errors, success.success
  order by error.date_part;"""

# Database to connect to
DBNAME = "news"

def q1(): #Goes through
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(questions[0])
    results = cursor.fetchall()
    print(results)
    conn.close()

def q2():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(questions[1])
    results = cursor.fetchall()
    print(results)
    conn.close()

def q3():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(questions[2])
    results = cursor.fetchall()
    print(results)
    conn.close()

q1()
q2()
q3()
#print(connect(author_sum))
#print(connect2(author_sum))

#print connect()
#print(connect)("select * from author_sum")


# python3 log_analysis.py
# psql -d news
# select * from author_sum;
