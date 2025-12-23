# # send_email.py
# import os
# from dotenv import load_dotenv
# import yagmail
# from fetch_quote import get_quote

# load_dotenv()

# EMAIL = os.getenv("EMAIL_ADDRESS")
# PASSWORD = os.getenv("EMAIL_PASSWORD")
# SMTP = os.getenv("SMTP_SERVER")
# PORT = int(os.getenv("SMTP_PORT", "587"))

# def send_test(to_address):
#     yag = yagmail.SMTP(user=EMAIL, password=PASSWORD, host=SMTP, port=PORT)
#     quote = get_quote() or "Keep going — no quote available right now."
#     subject = "ZenQuotes — Test Email"
#     body = f"Hello,\n\nHere is a test quote:\n\n{quote}\n\n— Sent via ZenQuotes Emailer"
#     yag.send(to=to_address, subject=subject, contents=body)
#     print(f"✅ Test email sent to {to_address}")

# if __name__ == "__main__":
#     # send to yourself for testing
#     send_test(EMAIL)


# import os
# import yagmail
# from dotenv import load_dotenv

# load_dotenv()

# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# SENDER_NAME = os.getenv("SENDER_NAME")

# def send_test(to_address):
#     subject = "Test Email from ZenQuotes App"
#     body = "✅ Hello! This is a test email sent using Python and Gmail SMTP."

#     yag = yagmail.SMTP(
#         user=EMAIL_ADDRESS,
#         password=EMAIL_PASSWORD,
#         host=SMTP_SERVER,
#         port=SMTP_PORT,
#         smtp_starttls=True,   # Use STARTTLS for port 587
#         smtp_ssl=False
#     )

#     yag.send(to=to_address, subject=subject, contents=body)
#     print(f"✅ Test email sent to {to_address}")

# send_test(EMAIL_ADDRESS)








# def send_daily_quotes():
#     import os
#     import yagmail
#     import sqlite3
#     from dotenv import load_dotenv
#     from fetch_quote import get_quote  # your quote fetcher

#     load_dotenv()

#     EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
#     EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
#     SMTP_SERVER = os.getenv("SMTP_SERVER")
#     SMTP_PORT = int(os.getenv("SMTP_PORT"))
#     SENDER_NAME = os.getenv("SENDER_NAME")

#     # Connect to DB and get active subscribers
#     conn = sqlite3.connect('subscribers.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, email FROM users WHERE subscription_status='active'")
#     users = cursor.fetchall()
#     conn.close()

#     quote = get_quote() or "Keep going — no quote available right now."
#     subject = "Your Daily Motivation"

#     yag = yagmail.SMTP(
#        yag = yagmail.SMTP(
#     user=EMAIL_ADDRESS,
#     password=EMAIL_PASSWORD,
#     host=SMTP_SERVER,
#     port=SMTP_PORT,
#     smtp_starttls=False,
#     smtp_ssl=True
# )

#     )

#     for name, email in users:
#         body = f"Hello {name},\n\nHere is your daily quote:\n\n{quote}\n\n— Sent via {SENDER_NAME}"
#         try:
#             yag.send(to=email, subject=subject, contents=body)
#             print(f"✅ Quote sent to {email}")
#         except Exception as e:
#             print(f"❌ Failed to send to {email}: {e}")

# # Optional: allow running directly
# if __name__ == "__main__":
#     send_daily_quotes()


# import os
# import sqlite3
# import yagmail
# from dotenv import load_dotenv
# from fetch_quote import get_quote

# load_dotenv()

# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = int(os.getenv("SMTP_PORT"))
# SENDER_NAME = os.getenv("SENDER_NAME")

# def send_daily_quotes():
#     # Connect to DB and get active subscribers
#     conn = sqlite3.connect('subscribers.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, email FROM users WHERE subscription_status='active'")
#     users = cursor.fetchall()
#     conn.close()

#     quote = get_quote() or "Keep going — no quote available right now."
#     subject = "Your Daily Motivation"

#     yag = yagmail.SMTP(
#         user=EMAIL_ADDRESS,
#         password=EMAIL_PASSWORD,
#         host=SMTP_SERVER,
#         port=SMTP_PORT,
#         smtp_starttls=False,   # For port 587
#         smtp_ssl=True,
#         oauth2_file=None      # Avoid looking for ~/.yagmail
#     )

#     for name, email in users:
#         body = f"Hello {name},\n\nHere is your daily quote:\n\n{quote}\n\n— Sent via {SENDER_NAME}"
#         try:
#             yag.send(to=email, subject=subject, contents=body)
#             print(f"✅ Quote sent to {email}")
#         except Exception as e:
#             print(f"❌ Failed to send to {email}: {e}")

# # Optional: run directly for testing
# if __name__ == "__main__":
#     send_daily_quotes()


import os
import sqlite3
import yagmail
import logging
from dotenv import load_dotenv
from fetch_quote import get_quote

import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_NAME = os.getenv("SENDER_NAME")

# ✅ Create a logs folder automatically if it doesn’t exist
os.makedirs("logs", exist_ok=True)

# ✅ Set up logging
logging.basicConfig(
    filename="logs/email.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_daily_quotes():
    try:
        # Connect to DB and get active subscribers
        conn = sqlite3.connect('subscribers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, email FROM users WHERE subscription_status='active'")
        users = cursor.fetchall()
        conn.close()

        if not users:
            logging.info("No active subscribers found.")
            print("⚠️ No active subscribers found.")
            return

        quote = get_quote() or "Keep going — no quote available right now."
        subject = "Your Daily Motivation"

        yag = yagmail.SMTP(
            user=EMAIL_ADDRESS,
            password=EMAIL_PASSWORD,
            host=SMTP_SERVER,
            port=SMTP_PORT,
            smtp_starttls=False,   # Using SSL
            smtp_ssl=True,
            oauth2_file=None       # Avoid looking for ~/.yagmail
        )

        for name, email in users:
            body = f"Hello {name},\n\nHere is your daily quote:\n\n{quote}\n\n— Sent via {SENDER_NAME}"
            try:
                yag.send(to=email, subject=subject, contents=body)
                msg = f"✅ Quote sent to {email}"
                print(msg)
                logging.info(msg)
            except Exception as e:
                msg = f"❌ Failed to send to {email}: {e}"
                print(msg)
                logging.error(msg)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"⚠️ Unexpected error: {e}")

# Optional: run directly for testing
if __name__ == "__main__":
    send_daily_quotes()
