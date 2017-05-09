#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

def connect(query):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  print(c.fetchall())
  db.close()

connect("select 2 + 2;")
