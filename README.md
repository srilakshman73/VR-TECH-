# VR TECH Solutions - Web Application

This repository contains the completely refactored full-stack Django application for VR TECH Solutions. It includes the required structure for deployment into a production environment.

## Features
- **Custom Apps**: Includes robust apps for `accounts`, `core`, `services`, `products`, `gallery`, `testimonials`, `contact`, and `blog`.
- **UI/UX**: Responsive HTML5 + CSS3 templates powered by Django templating with inheritance.
- **Authentication**: Built-in Django authentication supporting registration, login, logout, and password recovery.
- **Admin Dashboard**: Full CRUD management of all models via Django's integrated, customizable Admin dashboard.
- **Production-Ready**: Configured for Docker, Gunicorn, PostgreSQL, and Nginx.

## Installation Guide (Local Development)

### 1. Prerequisites
Ensure you have Python 3.13+ installed. We recommend setting up a virtual environment.

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Copy `.env.example` to a new file named `.env` and fill in your details:
```bash
cp .env.example .env
```
Ensure `DEBUG=True` for local development. Note: The app defaults to SQLite locally unless a proper `DATABASE_URL` is set, but it is optimized for PostgreSQL.

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/`. You can access the dashboard at `/admin/`.

---

## Deployment Instructions (Gunicorn + Nginx)

This project includes a `Dockerfile` and `docker-compose.yml` for quick Docker deployments, alongside standard `gunicorn` configurations.

### Running with Docker (Preferred)
```bash
docker-compose up --build -d
```

### Manual Deployment via Gunicorn & Nginx
If you are deploying manually onto a Linux server (Ubuntu/Debian):

1. Clone the repository and install requirements.
2. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
3. Set up a Systemd socket and service for Gunicorn to bind to `vr_tech.wsgi:application`.
4. Configure Nginx to reverse proxy traffic to your Gunicorn socket:
   ```nginx
   server {
       listen 80;
       server_name your_domain.com;

       location = /favicon.ico { access_log off; log_not_found off; }
       
       # Serve Static Files
       location /static/ {
           root /path/to/your/VR-TECH/staticfiles;
       }

       # Serve Media Files
       location /media/ {
           root /path/to/your/VR-TECH/media;
       }

       location / {
           proxy_set_header Host $http_host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_pass http://unix:/run/gunicorn.sock;
       }
   }
   ```
5. Secure your server with SSL via Let's Encrypt (Certbot).
