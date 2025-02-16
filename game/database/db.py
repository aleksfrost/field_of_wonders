import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#DB parametres to conect to DB

USER = 'yacu'
PASS = 'leonid'
HOST = '127.0.0.1'
DB_NAME = 'field_of_wonders'
PORT = '5432'

connection = psycopg2.connect(
    user=USER,
    password=PASS,
    host=HOST,
    port=PORT,
    database=DB_NAME,
)

def request_from_db(stmnt):
    with connection.cursor() as conn:
        conn.execute(stmnt)
        record = conn.fetchall()
        return record

def request_into_db(stmnt):
    with connection.cursor() as conn:
        conn.execute(stmnt)
        connection.commit()
