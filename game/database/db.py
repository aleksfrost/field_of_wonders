import psycopg2
from psycopg2 import Error

#DB parametres to conect to DB

USER = 'yacu'
PASS = 'leonid'
HOST = '127.0.0.1'
DB_NAME = 'field_of_wonders'
PORT = '5432'

conn =  psycopg2.connect(
    user=USER,
    password=PASS,
    host=HOST,
    port=PORT,
    database=DB_NAME,
)

def request_from_db(stmnt):
    with conn.cursor() as cur:
        cur.execute(stmnt)
        record = cur.fetchall()
        return record

def request_into_db(stmnt):
    with conn.cursor() as cur:
        try:
            cur.execute(stmnt)
            conn.commit()
        except Error as e:
            conn.rollback()
            print(f"Transaction failed: {e.pgcode} - {e.pgerror}")

