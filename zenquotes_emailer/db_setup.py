import sqlite3

# Connect to the database (creates file if it doesn't exist)
conn = sqlite3.connect("subscribers.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    subscription_status TEXT NOT NULL DEFAULT 'active',
    frequency TEXT NOT NULL DEFAULT 'daily'
)
""")

conn.commit()
print("✅ users table created successfully!")

conn.close()
