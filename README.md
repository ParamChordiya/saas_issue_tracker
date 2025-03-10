# SaaS Issue Tracker and Debugging Tool

## Project Overview
This **SaaS Issue Tracker and Debugging Tool** is designed to simulate real-world debugging for SaaS applications. It provides a **Flask API** for logging errors, a **Streamlit dashboard** for issue triaging, and **Celery** for automated issue resolution.

---

## Viewing Errors in Streamlit Dashboard

After starting the Streamlit dashboard, you can:

* **Filter errors** by severity (Low, Medium, High)
* **Mark issues** as Resolved, In Progress, or Escalated
* **Get real-time updates** on error occurrences

---

## Project Structure

# SaaS-Issue-Tracker/
```sh
│── backend/ 
│   │── app.py 
│   │── database.py 
│   │── logger.py 
│   │── models.py 
│   │── services.py 
│   └── tasks.py
│── frontend/ 
│   │── dashboard.py 
│   └── config.py
│── requirements.txt
│── README.md 
│── run.sh
│── celery_worker.sh
└── .env 
```

---

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** Streamlit
- **Database:** SQLite (SQLAlchemy)
- **Logging:** Python `logging` module
- **Automation:** Celery, Redis

---

## Features
**Real-time error logging** (Flask API)  
**Streamlit dashboard for tracking errors**  
**Error triaging (Resolved, In Progress, Escalated)**  
**Automated resolution for recurring issues**  
**High-severity error notifications**  

---

## Step-by-Step Execution Guide

### 1️. Clone the Repository
```sh
git clone https://github.com/ParamChordiya/saas_issue_tracker.git
cd SaaS-Issue-Tracker
```

### 2️. Set Up a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Start Redis

```sh
redis-server
```

### 5. Start Celery Worker

```sh
bash celery_worker.sh
```

### 6. Run Backend and Frontend
```sh
bash run.sh
```

### 7. Log an Error Example
``` sh
curl -X POST "http://127.0.0.1:5000/log_error" \
     -H "Content-Type: application/json" \
     -d '{
          "error_type": "Database Connection Error",
          "severity": "High",
          "message": "Failed to connect to the database"
         }'
```

