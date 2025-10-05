#!/bin/bash

echo "🏥 Starting Dr. Shahan Medical Portfolio..."
echo "📋 Setting up the environment..."

# Install dependencies if not already installed
if [ ! -d ".venv" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Run migrations
echo "🗄️ Setting up database..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if none exists (optional)
echo "👨‍⚕️ Creating admin user (optional)..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

echo "🚀 Starting Django development server..."
echo "📱 Your medical portfolio will be available shortly!"
echo "🔗 Access the admin panel at: /admin/ (username: admin, password: admin123)"
echo ""

# Start the server
python manage.py runserver 0.0.0.0:8000