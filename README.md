## Overview

The **Note Like Us** application allows users to create, edit, and manage notes.

## Technology Stack

### Backend
- **Django REST Framework**
- **Sentiment Analysis NLP Model**

### Frontend
- **React**
- **Bootstrap**

## Sentiment Analysis Functionality

The sentiment analysis feature processes user notes to assess their emotional tone. It categorizes notes as positive, neutral, or negative and provides a score. This functionality is implemented in the `signals.py` file with a pre-trained sentiment analysis model.

## Getting Started

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/scott062/note_like_us.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd note_like_us
   ```

3. **Set up local .env file**
   Before the project can be started, please update your personal `.env` file at the root of the project to include the expected environment variables (and appropriate values):
   ```
   DJANGO_SECRET_KEY
   POSTGRES_DB
   POSTGRES_USER
   POSTGRES_PASSWORD
   DATABASE_HOST
   DATABASE_PORT
   ```
   Notes:
   * Database is POSTGRES, but can be swapped with minor config changes in settings.py

4. **Running API (Docker-Compose):**
   ```bash
   docker-compose up --build
   ```
   * Docker running services should alert you of any misconfigurations if the .env is not properly configured

5. **Migrate DB:**
   ```bash
   docker-compose run web python manage.py migrate
   ```
   stop the service and restart
   ```bash
   docker-compose up
   ```

If everything is running properly, you should be able to access the running django service at localhost:8000. You can curl, use postman, or access the django admin site to begin quickly testing endpoints.

Otherwise, you can setup a lightweight react frontend at this link: https://github.com/scott062/note_like_us_frontend.

   The backend server should now be running on `http://localhost:8000`.

### Frontend Setup

1. **Clone the frontend repository:**
   ```bash
   git clone https://github.com/scott062/note_like_us_frontend.git
   ```

2. **Navigate to the frontend directory:**
   ```bash
   cd note_like_us_frontend
   ```

3. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

4. **Start the frontend development server:**
   ```bash
   npm start
   ```

   The frontend application should now be accessible at `http://localhost:3000`.
