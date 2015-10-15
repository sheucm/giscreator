# Gis Creator
demo on heroku: https://giscreator.herokuapp.com/

## Requirement:
dj-database-url==0.3.0
dj-static==0.0.6
Django==1.7.10
gunicorn==19.3.0
static3==0.6.1
wheel==0.24.0
psycopg2==2.5.4  //if it deploys on heroku



## How to use on local:
- Git clone our project.
- Install Virtualenv and get in the virtual environment.
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- Open the browser with 127.0.0.1:8000/
