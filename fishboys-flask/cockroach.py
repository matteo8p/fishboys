import os
import psycopg2

DATABASE_URL="postgresql://matt:Qd9RhxiNMvQDZOcwq44ZPw@free-tier11.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dbulky-shaman-2489"
conn = psycopg2.connect(DATABASE_URL)

query = "UPDATE fishdb.fish SET name = 'sturgeon' WHERE name = 'atlantic_sturgeon';"
with conn.cursor() as cur:
    cur.execute(query)
    # res = cur.fetchall()
    conn.commit()
    # return res

