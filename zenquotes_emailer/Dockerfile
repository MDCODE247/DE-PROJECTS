# 1. Use a lightweight Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Copy dependency list
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY . .

# 7. Run the scheduler
CMD ["python", "scheduler.py"]
