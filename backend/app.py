from flask import Flask, request, jsonify
from database import db_session, init_db
from models import ErrorLog
from logger import log_error
import tasks

app = Flask(__name__)

@app.route('/log_error', methods=['POST'])
def log_error_route():
    """API to log an error with severity"""
    data = request.json
    error_type = data.get('error_type')
    severity = data.get('severity', 'Low')
    message = data.get('message', '')

    error_entry = log_error(error_type, severity, message)
    db_session.add(error_entry)
    db_session.commit()

    if severity.lower() == 'high':
        tasks.notify_admin.delay(message)

    return jsonify({'status': 'Error Logged', 'error_id': error_entry.id})

@app.route('/errors', methods=['GET'])
def get_errors():
    """API to fetch all errors"""
    errors = ErrorLog.query.all()
    return jsonify([error.to_dict() for error in errors])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
