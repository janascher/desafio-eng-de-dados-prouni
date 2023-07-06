import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def select_sexo():
    conn = psycopg2.connect(
    host=os.getenv('db_host'),
    database=os.getenv('db_name'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password')
)
    sql = "SELECT sexo, COUNT(*) AS count FROM Beneficiarios GROUP BY sexo"
    count_sex = pd.read_sql_query(sql, conn)
    conn.close()
    return count_sex

def select_raca():
    conn = psycopg2.connect(
    host=os.getenv('db_host'),
    database=os.getenv('db_name'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password')
)
    sql = "SELECT raca, COUNT(*) AS count FROM Beneficiarios GROUP BY raca"
    count_race = pd.read_sql_query(sql, conn)
    conn.close()
    return count_race

print(select_sexo())
print(select_raca())