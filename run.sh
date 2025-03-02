#!/bin/bash
echo "Starting Flask API..."
python backend/app.py &
echo "Starting Streamlit Dashboard..."
streamlit run frontend/dashboard.py
