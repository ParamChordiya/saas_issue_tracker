#!/bin/bash
echo "Starting Celery worker..."
celery -A backend.tasks worker --loglevel=info
