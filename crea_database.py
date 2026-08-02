import pandas as pd
import sqlite3

df = pd.read_csv("aziende_con_rischio.csv")
conn = sqlite3.connect("aziende.db")
df.to_sql("aziende", conn, if_exists="replace", index=False)
conn.close()

print("Database creato! Tabella 'aziende' pronta.")