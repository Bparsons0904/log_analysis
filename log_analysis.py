#!/usr/bin/env python3

import psycopg2
import string  # Used to capatilize articles first letter

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
select error.date, error.errors, success.success
  from error, success
  where error.date=success.date and
  error.errors/(error.errors + success.success)::float > .01
  group by error.date, error.errors, success.success
  order by error.date;"""

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


def q1():  # Run query for question 1
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question1)
    results = cursor.fetchall()
    q1_results.append(results)
    conn.close()


def q2():  # run query for question 2
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question2)
    results = cursor.fetchall()
    q2_results.append(results)
    conn.close()


def q3():  # run query for question 3
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(question3)
    results = cursor.fetchall()
    q3_results.append(results)
    conn.close()


def q1_format():  # formating function for article titles
    count = 0
    result = []
    while count < 3:
        formated = q1_results[0][count][0].replace("-", " ")
        formated = string.capwords(formated)
        result.append(formated)
        count += 1
    return result


def q1_print():  # print solution for problem 1
    articles = q1_format()
    print("\nThe 3 most popular articles:")
    print('"' + articles[0] + '" - ' + str(q1_results[0][0][1]) + ' views')
    print('"' + articles[1] + '" - ' + str(q1_results[0][1][1]) + ' views')
    print('"' + articles[2] + '" - ' + str(q1_results[0][2][1]) + ' views\n')


def q2_print():  # print solution for problem 2
    print("The 3 most popular author's:")
    print(q2_results[0][0][0] + '" - ' + str(int(q2_results[0][0][1])) +
          ' views')
    print(q2_results[0][1][0] + '" - ' + str(int(q2_results[0][1][1])) +
          ' views')
    print(q2_results[0][2][0] + '" - ' + str(int(q2_results[0][2][1])) +
          ' views\n')


def q3_print():  # print solution for question 3
    print("Days with more than 1% of request that lead to an error:")
    error_rate = (q3_results[0][0][1]/q3_results[0][0][2])*100
    error_rate = format(error_rate, '.2f')
    print(str(q3_results[0][0][0]) + ' - ' + str(error_rate) + '%\n')


def run_scripts():
    q1()
    q2()
    q3()
    q1_print()
    q2_print()
    q3_print()

run_scripts()
