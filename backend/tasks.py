from celery import Celery
import time

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def notify_admin(error_message):
    """Send a mock notification to the admin"""
    print(f"🔔 CRITICAL ALERT: {error_message}")

@celery.task
def restart_service():
    """Simulate restarting a failing service"""
    print("🔄 Restarting the mock service...")
    time.sleep(2)
    print("✅ Service restarted successfully!")
