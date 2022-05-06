import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import login_date

conn = psycopg2.connect(
        user=login_date['lar_nout']['login'],
        password=login_date['lar_nout']['password']
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute('create database quiz_quest')
cursor.close()
conn.close()



