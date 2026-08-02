import pandas as pd
import sqlite3

with open("sql/rischio_per_fascia.sql") as f:
    query = f.read()

conn = sqlite3.connect("aziende.db")
risultato = pd.read_sql(query, conn)
conn.close()

print(risultato)