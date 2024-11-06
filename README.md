# Starting Project

## Env Variables
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

## Running API (Docker-Compose)
Once .env is properly setup, the API can be run locally with:
```
docker-compose up --build
```
* Docker running services should alert you of any misconfigurations if the .env is not properly configured

Once the application has been built, you will want to migrate your DB using the following command:
```
docker-compose run web python manage.py migrate
```
and then, restart everything to confirm it all works:
```
docker-compose up
```

If everything is running properly, you should be able to access the running django service at localhost:8000. You can curl, use postman, or access the django admin site to begin quickly testing endpoints.

Otherwise, you can setup a lightweight react frontend at this link: https://github.com/scott062/note_like_us_frontend.
