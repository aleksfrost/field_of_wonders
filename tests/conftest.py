import sqlite3
import psycopg2
import pytest

from unit.tables_script import querry

# Фикстура для подключения к базе данных и создания временной таблицы


USER = 'yacu'
PASS = 'leonid'
HOST = '127.0.0.1'
DB_NAME = 'test_fow'
PORT = '5432'


@pytest.fixture
def db_connection():
    conn = psycopg2.connect(
        user=USER,
        password=PASS,
        host=HOST,
        port=PORT,
        database=DB_NAME,
    )

    cursor = conn.cursor()
    cursor.execute(querry)
    conn.commit()

    yield conn

    conn.close()