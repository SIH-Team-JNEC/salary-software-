import sqlite3
import os

# Define the path to the database file
db_path = os.path.join(os.path.dirname(__file__), 'users.db')

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table for users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    blood_grp TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

def add_user(username, email, bg):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, blood_grp) VALUES (?, ?, ?)', (username, email, bg))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users