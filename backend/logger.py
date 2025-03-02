import logging
from models import ErrorLog

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(error_type, severity, message):
    """Log an error to the database"""
    logging.error(f"{error_type} - {severity}: {message}")
    return ErrorLog(error_type=error_type, severity=severity, message=message)
