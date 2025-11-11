# import schedule
# import time
# from send_email import send_daily_quotes  # import your function

# # Schedule the task every day at 7 AM
# schedule.every(1).minutes.do(send_daily_quotes)

# print("🕒 Scheduler started. Waiting for 7 AM...")

# while True:
#     schedule.run_pending()
#     time.sleep(5)  # check every 30 seconds



# import schedule
# import time
# from send_email import send_daily_quotes

# # For testing, run every 1 minute (change to daily at 7 AM later)
# # schedule.every().day.at("07:00").do(send_daily_quotes)

# # print("🕒 Scheduler started. Running every minute for testing...")
# print("🕒 Scheduler started. Running every 07:00 minutes for testing...")
# while True:
#     schedule.run_pending()
#     time.sleep(30)  # check every 5 seconds

# schedule.every().day.at("07:00").do(send_daily_quotes)

# import logging
# import os

# # create log folder if not exist
# os.makedirs("logs", exist_ok=True)

# logging.basicConfig(
#     filename="logs/scheduler.log",
#     level=logging.INFO,
#     format="%(asctime)s — %(levelname)s — %(message)s"
# )
# import schedule
# import time
# import logging
# from datetime import datetime
# from send_email import send_daily_quotes

# # --- Configure logging ---
# logging.basicConfig(
#     filename="logs/scheduler.log",  # where logs will be saved
#     level=logging.INFO,             # record all info and errors
#     format="%(asctime)s — %(levelname)s — %(message)s"
# )

# def job():
#     logging.info("Running send_daily_quotes()")
#     try:
#         send_daily_quotes()
#         logging.info("✅ Daily quotes sent successfully")
#     except Exception as e:
#         logging.error(f"❌ Error sending quotes: {e}")

# # --- Scheduler setup ---
# # For testing: run every 1 minute
# schedule.every().day.at("07:00").do(send_daily_quotes)
# print("🕒 Scheduler started. See you at 07.00 am")
# logging.info("🕒 Scheduler started.")

# while True:
#     schedule.run_pending()
#     time.sleep(10)



# import schedule
# import time
# import logging
# from datetime import datetime
# import glob
# import os
# from send_email import send_daily_quotes # import your functions

# # --- Step 1: Prepare logs folder and log rotation ---
# os.makedirs("logs", exist_ok=True)

# # Rotate logs larger than 5 MB
# log_files = glob.glob("logs/*.log")
# for log_file in log_files:
#     if os.path.getsize(log_file) > 5 * 1024 * 1024:  # 5 MB
#         timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#         os.rename(log_file, f"{log_file}.{timestamp}")

# # --- Step 2: Configure logging ---
# logging.basicConfig(
#     filename="logs/scheduler.log",
#     level=logging.INFO,
#     format="%(asctime)s — %(levelname)s — %(message)s"
# )

# # --- Step 3: Define the job function ---
# def job():
#     logging.info("Running send_daily_quotes()")
#     try:
#         send_daily_quotes()
#         logging.info("✅ Daily quotes sent successfully")
#     except Exception as e:
#         logging.error(f"❌ Error sending daily quotes: {e}")
#         # Notify admin by email about the failure
#         try:
#             send_test("your.email@gmail.com")  # replace with your admin email
#             logging.info("Admin notified about the failure")
#         except Exception as ex:
#             logging.error(f"❌ Failed to notify admin: {ex}")

# # --- Step 4: Schedule the job ---
# schedule.every().day.at("07:00").do(job)  # runs at 7 AM system time

# print("🕒 Scheduler started. Waiting for 7 AM...")
# logging.info("🕒 Scheduler started. Waiting for 7 AM...")

# # --- Step 5: Keep scheduler running ---
# while True:
#     schedule.run_pending()
#     time.sleep(10)  # check every 10 seconds


import schedule
import time
import logging
from datetime import datetime
import glob
import os
from send_email import send_daily_quotes  # only the function we have now

# --- Step 1: Prepare logs folder and log rotation ---
os.makedirs("logs", exist_ok=True)

# Rotate logs larger than 5 MB
log_files = glob.glob("logs/*.log")
for log_file in log_files:
    if os.path.getsize(log_file) > 5 * 1024 * 1024:  # 5 MB
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        os.rename(log_file, f"{log_file}.{timestamp}")

# --- Step 2: Configure logging ---
logging.basicConfig(
    filename="logs/scheduler.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# --- Step 3: Define the job function ---
def job():
    logging.info("Running send_daily_quotes()")
    try:
        send_daily_quotes()
        logging.info("✅ Daily quotes sent successfully")
    except Exception as e:
        logging.error(f"❌ Error sending daily quotes: {e}")

# --- Step 4: Schedule the job ---
schedule.every().day.at("07:00").do(job)  # runs at 7 AM system time
# In scheduler.py (for testing)
# schedule.every(1).minutes.do(job)

print("🕒 Scheduler started. Waiting for 7 AM...")
logging.info("🕒 Scheduler started. Waiting for 7 AM...")

# --- Step 5: Keep scheduler running ---
while True:
    schedule.run_pending()
    time.sleep(10)  # check every 10 seconds