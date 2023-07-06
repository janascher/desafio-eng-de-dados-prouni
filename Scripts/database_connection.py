import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    conn = psycopg2.connect(
        host=os.getenv('db_host'),
        database=os.getenv('db_name'),
        user=os.getenv('db_user'),
        password=os.getenv('db_password')
    )
    return conn
