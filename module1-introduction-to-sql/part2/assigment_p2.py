import pandas as pd
import os 
import sqlite3


data = pd.read_csv('/Users/keinobaird/Desktop/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holiday.sqlite3')
curs = conn.cursor()

#Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
query_1a = 'DROP TABLE review'
curs.execute(query_1a)
data.index.name = 'id'

#print(data.columns) 

pd.DataFrame.to_sql(self = data, name = "review", con = conn, index=True)



query_1 = 'SELECT COUNT(id) FROM review;'
print(curs.execute(query_1).fetchone())

#query_1a = 'DROP TABLE review'
# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 
# in the Shopping category?

#query_2 = 'SELECT nature,Shopping FROM review WHERE nature=100 AND Shopping=100;'

# What are the average number of reviews for each category?
'''
query_3a = 'SELECT AVG(Sports)from review;'
query_3b = 'SELECT AVG(Religious)from review;'
query_3c = 'SELECT AVG(Nature)from review;'
query_3d = 'SELECT AVG(Shopping)from review;'
query_3e = 'SELECT AVG(Theatre)from review;'
query_3f = 'SELECT AVG(Picnic)from review;'
'''