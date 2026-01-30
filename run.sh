#!/bin/bash

cd /home/coder/workspace/webapp

# Activate virtual environment if exists
if [ -d "/home/coder/workspace/.venv" ]; then
    source /home/coder/workspace/.venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt -q

# Run migrations
python manage.py migrate

# Load sample data if needed
python manage.py load_sample_data 2>/dev/null || echo "Sample data already loaded"

# Run server
echo "Starting Django server at http://localhost:8000"
echo "Admin: http://localhost:8000/admin"
echo "Press Ctrl+C to stop"
python manage.py runserver 0.0.0.0:8000
