import pandas as pd
import sqlite3

# Load CSV files
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Save to SQLite DB
conn = sqlite3.connect("ipl_data.db")
matches.to_sql("matches", conn, if_exists="replace", index=False)
deliveries.to_sql("deliveries", conn, if_exists="replace", index=False)
conn.close()

print("✅ Database created successfully")

