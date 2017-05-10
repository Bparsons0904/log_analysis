#!/usr/bin/env python3

import psycopg2
import string

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

# from psycopg2 documentation, uses float instead of DECIMAL as part of return
DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)
psycopg2.extensions.register_type(DEC2FLOAT)

q1_results = []
q2_results = []
q3_results = []

def q1(): #Goes through
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question1)
    results = cursor.fetchall()
    q1_results.append(results)
    conn.close()

def q2():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question2)
    results = cursor.fetchall()
    q2_results.append(results)
    conn.close()

def q3():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question3)
    results = cursor.fetchall()
    q3_results.append(results)
    conn.close()

def q1_format():
    count = 0
    result = []
    while count < 3:
        formated = q1_results[0][count][0].replace("-", " ")
        formated = string.capwords(formated)
        result.append(formated)
        count += 1
    return result

def q1_print():
    articles = q1_format()
    print("The 3 most popular articles:")
    print('"'+articles[0]+'" - '+ str(q1_results[0][0][1]) +' views')
    print('"'+articles[1]+'" - '+ str(q1_results[0][1][1]) +' views')
    print('"'+articles[2]+'" - '+ str(q1_results[0][2][1]) +' views\n')

def q2_format:
    result = []
    

def q2_print():
    print("The 3 most popular author's:")
    print('"'+q2_results[0][0][0]+'" - '+ str(q2_results[0][0][1]) +' views')
    print('"'+q2_results[0][1][0]+'" - '+ str(q2_results[0][1][1]) +' views')
    print('"'+q2_results[0][2][0]+'" - '+ str(q2_results[0][2][1]) +' views\n')

def run_scripts():
    q1()
    q2()
    q3()
    q1_print()
    q2_print()

run_scripts()


# python3 log_analysis.py
# psql -d news
# select * from author_sum;
