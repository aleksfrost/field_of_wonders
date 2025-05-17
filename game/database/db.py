import psycopg2
from psycopg2 import Error

#DB parametres to conect to DB

# USER = 'yacu'
# PASS = 'leonid'
# HOST = '127.0.0.1'
# DB_NAME = 'field_of_wonders'
# PORT = '5432'

#conn_url
# postgresql://uexpm5qfixhcxfjwp50k:6aFidgcZOm092zulJ0hQxKZwnPPot9@bal1qddamd6nblnqo8em-postgresql.services.clever-cloud.com:5432/bal1qddamd6nblnqo8em

HOST = "bal1qddamd6nblnqo8em-postgresql.services.clever-cloud.com"
DB_NAME = "bal1qddamd6nblnqo8em"
USER = "uexpm5qfixhcxfjwp50k"
PASS = "6aFidgcZOm092zulJ0hQxKZwnPPot9"
PORT = "5432"



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

