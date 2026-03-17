import sqlite3

conn = sqlite3.connect("fitness.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY,
username TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS weights(
user_id INTEGER,
weight REAL,
date TEXT
)
""")

conn.commit()