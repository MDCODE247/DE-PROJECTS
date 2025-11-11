# ZenQuotes Emailer

Automated quote delivery platform that sends daily motivational quotes to subscribed users via email. Built for **MindFuel**, a mental wellness startup.

---

## **Project Overview**

The ZenQuotes Emailer allows users to receive a daily quote every morning at 7 AM. Users can subscribe through a simple web dashboard, and all activities are logged for monitoring.  

**Key features:**
- Fetch quotes from [ZenQuotes API](https://zenquotes.io/)
- Send personalized emails to subscribers
- Web dashboard for managing subscriptions
- Logging and error handling
- Scheduling emails to send daily at 7 AM

---

## **Tools & Technologies Used**

| Tool/Technology | Purpose |
|-----------------|---------|
| Python 3.14     | Main programming language |
| SQLite          | Database for storing subscribers |
| Flask           | Web dashboard for subscription management |
| Yagmail         | Sending emails via Gmail SMTP |
| python-dotenv   | Load environment variables from `.env` file |
| schedule        | Task scheduler for sending emails daily |
| HTML/CSS        | Dashboard templates (frontend) |

---

## **Project Setup**

### **1. Clone the repository**
```bash
git clone <repository_url>
cd zenquotes_emailer
```

### **2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### **3. Install dependencies**
```bash
pip install Flask yagmail python-dotenv schedule Flask-WTF
```

### **4. Configure environment variables**
Create a `.env` file in the project root with the following:
```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
SENDER_NAME=ZenQuotesEmailer
```

### **5. Setup database**
Run the database setup script:
```bash
python db_setup.py
```
This will create `subscribers.db` and the `users` table.

---

## **Project Structure**

```
zenquotes_emailer/
│
├── dashboard.py          # Flask web dashboard
├── send_email.py         # Email sending logic
├── fetch_quote.py        # Fetch quote from ZenQuotes API
├── scheduler.py          # Scheduler to send daily emails
├── db_setup.py           # Initialize database
├── subscribers.db        # SQLite database
├── .env                  # Environment variables
├── templates/            # HTML templates
│   ├── index.html
│   └── subscribe.html
├── static/               # Optional CSS/JS
└── venv/                 # Virtual environment
```

---

## **Running the Project**

### **1. Start the Flask Dashboard**
```bash
python dashboard.py
```
- Open your browser at `http://127.0.0.1:5000/`  
- View subscribers or add new ones via `/subscribe`.

### **2. Test Email Sending**
```bash
python send_email.py
```
- Sends a test quote to the email defined in `.env`.

### **3. Run Scheduler**
```bash
python scheduler.py
```
- Automatically sends daily quotes to active subscribers at 7 AM.  
- For testing, you can temporarily schedule every 1 minute in `scheduler.py`.

---

## **Logging**

- Logs are stored in the `logs/` folder:
  - `scheduler.log` – Scheduler activity and errors
  - `email.log` – Email sending events
- Logs include timestamps, success/failure messages, and error details.

---

## **How it Works**

1. **Subscriber Management**
   - Users are added via the dashboard (`/subscribe`)  
   - Stored in `subscribers.db` with `subscription_status` and `frequency`  

2. **Quote Fetching**
   - `fetch_quote.py` connects to ZenQuotes API to get a daily quote  

3. **Email Sending**
   - `send_email.py` uses `yagmail` and Gmail SMTP  
   - Sends personalized quote emails to all active subscribers  

4. **Scheduler**
   - `scheduler.py` uses `schedule` to run `send_daily_quotes()` every day at 7 AM  

5. **Logging**
   - Every action is logged in `logs/` for monitoring and troubleshooting  

---

## **Roadmap / Possible Improvements**

- **Unsubscribe functionality** – allow users to opt-out via dashboard  
- **Frequency management** – let users choose daily or weekly emails  
- **Admin notifications** – send an email if sending fails to any subscriber  
- **Dashboard styling** – add CSS and a modern UI  
- **Deployment** – host scheduler/dashboard on a cloud server (PythonAnywhere, Render, AWS, etc.) for 24/7 availability  
- **Multiple SMTP providers** – allow flexibility beyond Gmail  
- **Email templates** – use HTML for richer formatted quotes  

---

## **Conclusion**

You now have a **fully functional ZenQuotes Emailer**:  
- Subscribers can be added through the dashboard  
- Quotes are sent automatically at 7 AM  
- Activity is logged  
- The project is easily extendable for future enhancements  
```

