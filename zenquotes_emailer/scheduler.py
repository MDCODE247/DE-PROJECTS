import requests
from dotenv import load_dotenv
import smtplib
import sqlite3

import schedule
import time
import logging
from datetime import datetime
import glob
import os
from send_email import send_daily_quotes

# 🔑 Load environment variables
load_dotenv()

# --- Step 1: Prepare logs folder and log rotation ---
os.makedirs("logs", exist_ok=True)

log_files = glob.glob("logs/*.log")
for log_file in log_files:
    if os.path.getsize(log_file) > 5 * 1024 * 1024:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        os.rename(log_file, f"{log_file}.{timestamp}")

# --- Step 2: Configure logging ---
logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# --- Step 3: Define the job ---
def job():
    logging.info("Running send_daily_quotes()")
    try:
        send_daily_quotes()
        logging.info("✅ Daily quotes sent successfully")
    except Exception as e:
        logging.error(f"❌ Error sending daily quotes: {e}")

# --- Step 4: Schedule the job ---
schedule.every().day.at("08:50").do(job)

print("🕒 Scheduler started. Waiting for scheduled time...")
logging.info("🕒 Scheduler started. Waiting for scheduled time...")

# --- Step 5: Keep scheduler running ---
while True:
    schedule.run_pending()
    time.sleep(10)
