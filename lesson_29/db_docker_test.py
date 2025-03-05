import psycopg2
import time

time.sleep(3)

conn = psycopg2.connect(
    dbname="postgres",
    user="anna",
    password="anna",
    host="db",
    port=5432
)
