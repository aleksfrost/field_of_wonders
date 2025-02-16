import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from parcer import parce_csv


USER = 'farmer'
PASS = 'farmer_pig'
HOST = '127.0.0.1'
DB_NAME = 'farmers_markets'
PORT = '5432'

connection = psycopg2.connect(
    user=USER,
    password=PASS,
    host=HOST,
    port=PORT,
    database=DB_NAME
)

def make_request(request):
    cursor = connection.cursor()
    cursor.execute(request)
    return cursor

record = make_request(
    f"""select market_id, market_name, country_name, city_name
        from markets
        join zips on markets.zip_id=zips.zip_id
        join countries on zips.zip_id=countries.zip_id
        join cities on zips.zip_id=cities.zip_id
        where "country_id"=2;
        """
    ).fetchall()
print()
print()
for rec in record:
    print(rec)
print()
print(record)
print()
print()



if connection:
    connection.close()
    print("Connection with PostgreSQL is closed")


#changes to DB needs to be commited "conn.commit()" to see it right now