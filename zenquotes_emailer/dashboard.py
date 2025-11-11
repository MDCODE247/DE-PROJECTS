from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

DB_FILE = "subscribers.db"

# --- Home page ---
@app.route("/")
def index():
    # Show all subscribers
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, subscription_status FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template("index.html", users=users)

# --- Subscribe form ---
@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            flash("Please provide both name and email.")
            return redirect(url_for("subscribe"))

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, subscription_status, frequency)
            VALUES (?, ?, 'active', 'daily')
        """, (name, email))
        conn.commit()
        conn.close()

        flash("Subscription successful!")
        return redirect(url_for("index"))

    return render_template("subscribe.html")

if __name__ == "__main__":
    app.run(debug=True)
