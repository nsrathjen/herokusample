1. create django project locally

2. create Procfile in django root:
	web: gunicorn myproject.wsgi --log-file -

2a. Create runtime.txt in django root:
	python-3.4.3u

3. install gunicorn with pip

4. install dj_database_url with pip

5. update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

6. if you need static files follow the directions to set up whitenoise

7. go to getting started with python on heroku

8. install the toolbelt (it says you need ruby but it will install ruby if you don't have it)

9. Skip prepare the app

10. Do heroku create to create a new app. Give credentials

11. git push heroku master

12. heroku run python manage.py makemigrations

13. heroku run python manage.py migrate

14. To connect yourself to the heroku database in case something goes wrong -
	DATABASE_URL=$(heroku config:get DATABASE_URL -a whatever_your_app_name_is)
	export DATABASE_URL