import sqlite3

def add_user(name, email, frequency="daily"):
    conn = sqlite3.connect("subscribers.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO users (name, email, frequency)
        VALUES (?, ?, ?)
        """, (name, email, frequency))
        conn.commit()
        print(f"✅ User {name} added successfully!")
    except sqlite3.IntegrityError:
        print(f"⚠️ User with email {email} already exists.")
    finally:
        conn.close()

# Test adding a user
if __name__ == "__main__":
    add_user("Mohammed", "ammedabubakard500@gmail.com")
