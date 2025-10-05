# Dr. Shahan Medical Portfolio

A professional Django-based portfolio website for medical practitioners to showcase before/after cases and services.

## Features

- 🏥 Professional medical portfolio design
- 📸 Before/After image galleries with interactive comparisons
- 📱 Fully responsive and mobile-friendly
- 🎨 Modern UI/UX with smooth animations
- 🔐 Admin panel for content management
- 📊 Case categorization and filtering
- 🌐 Production-ready deployment configuration

## Quick Demo

You can view this project online at: `[Your deployed URL will go here]`

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/drownsite.git
cd drownsite
```

2. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your local settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

## Deployment Options

### Option 1: Render (Recommended - Free)

1. Push your code to GitHub
2. Go to [Render.com](https://render.com)
3. Connect your GitHub repository
4. Set environment variables in Render dashboard
5. Deploy automatically!

**Environment Variables for Render:**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

### Option 2: Railway

1. Push to GitHub
2. Go to [Railway.app](https://railway.app)
3. Connect GitHub repo
4. Set environment variables
5. Deploy!

### Option 3: Heroku

1. Install Heroku CLI
2. Push to GitHub
3. Connect Heroku to GitHub repo
4. Set config vars (environment variables)
5. Deploy from GitHub

## Showing to Clients Without Your Laptop

### Method 1: Live Deployment (Best)
- Deploy to Render/Railway (free)
- Share the live URL with clients
- They can view it on any device with internet

### Method 2: GitHub Codespaces
- Client opens your GitHub repo
- Clicks "Code" > "Codespaces" > "Create codespace"
- Full development environment runs in their browser
- No local setup required!

### Method 3: Local Network Demo
- Run `python manage.py runserver 0.0.0.0:8000`
- Share your local IP address
- Client connects on same WiFi network

## Project Structure

```
drsite/
├── drsite/          # Main project settings
├── portfolio/       # Main application
│   ├── models.py    # Database models
│   ├── views.py     # View functions
│   ├── urls.py      # URL routing
│   ├── admin.py     # Admin configuration
│   └── templates/   # HTML templates
├── media/           # Uploaded images
├── static/          # Static files (CSS, JS)
├── requirements.txt # Python dependencies
├── Procfile        # Deployment configuration
└── manage.py       # Django management script
```

## Admin Panel

Access the admin panel at `/admin/` to:
- Manage doctor profiles
- Add/edit patient cases
- Upload before/after images
- Create before/after pairs
- Publish content

## Technology Stack

- **Backend:** Django 3.2
- **Database:** SQLite (development) / PostgreSQL (production)
- **Frontend:** Bootstrap 5, Custom CSS, JavaScript
- **Images:** Pillow for image processing
- **Deployment:** Gunicorn, WhiteNoise for static files

## Support

For questions or support, contact [your-email@example.com]

## License

This project is proprietary and confidential.