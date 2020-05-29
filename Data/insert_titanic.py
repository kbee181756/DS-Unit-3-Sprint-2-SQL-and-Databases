import os
import pandas as pd 
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Read csv 
url = 'https://raw.githubusercontent.com/kbee181756/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
titanic = pd.read_csv(url)
print(titanic.head())


# reads the contents of the .env file and adds them to the environment
load_dotenv() 

# Connect to Postgresql 
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(sql_url)


# Connection to Database
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
#print("CONNECTION", type(connection))
cursor = connection.cursor()
print("CURSOR", type(cursor))


titanic.to_sql('Titanic', engine, if_exists="replace")

#query_1 = 'SELECT COUNT("Survived"),"Survived" FROM"Titanic" GROUP BY"Survived"'
query_4 = 'SELECT AVG("Age"),"Pclass" FROM"Titanic" GROUP BY"Pclass"'
cursor.execute(query_4)
results = cursor.fetchall()
print(type(results))
print(results)

