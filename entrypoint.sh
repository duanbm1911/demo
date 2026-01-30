#!/bin/bash

echo "Waiting for database..."
python manage.py wait_for_db

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Loading sample data..."
python manage.py load_sample_data || echo "Sample data already loaded"

echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@hoguomopera.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
END

echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 webapp.wsgi:application
