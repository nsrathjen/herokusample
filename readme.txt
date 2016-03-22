1. create a django project locally

2. create a "Procfile" in django root:
	This must be located at the top level (that is, in the same folder as your manage.py script)
	The file should be called "Procfile" with no extension (Windows users beware, the OS will often hide your file extensions, and most editors will add a .txt to the file, so this step can cause problems)
	The file should contain exactly the following (except with "myproject.wsgi" replaced appropriately, see example for help)
	web: gunicorn myproject.wsgi --log-file -

3. Create a runtime.txt file in django root:
	Again, the location and name of the file matters a great deal.
	python-3.4.3

4. install gunicorn with pip
	Simply run "pip install gunicorn" in your command line. If "pip" isn't found, be sure Python and its scripts folder are on your Path.

5. install dj_database_url with pip	


6. Create a requirements.txt file in django root:
	The following would be the bare minimum contents, but depending on your project you may need to add more
	Django==1.8.8
	dj-database-url==0.4.0
	gunicorn==19.4.5
	psycopg2==2.6.1



7. update settings.py:

if os.environ.get('DATABASE_URL'):
	import dj_database_url
	db_from_env = dj_database_url.config(conn_max_age=500)
	DATABASES['default'].update(db_from_env)
else:
	DATABASES = {
	    'default': {
        	'ENGINE': 'django.db.backends.sqlite3',
        	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    		}
	}

8. if you need static files follow the directions to set up whitenoise

9. go to Getting Started with Python on Heroku (https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

10. Make a heroku account and install the toolbelt (it says you need ruby but it will install ruby if you don't have it)

11. Skip prepare the app, but if you haven't already, go to your Django root folder and do "git init" followed by "git add ." and "git commit"

12. Run "heroku create" in your command line to create a new app. Be sure you're in the django root folder when you do. This may take a minute, but you'll need to input your username/password so don't walk away.

13. git push heroku master

14. heroku run "python manage.py makemigrations [appname] && python manage.py migrate [appname]" (INCLUDING THE QUOTES)

16. To connect yourself to the heroku database in case something goes wrong -
	DATABASE_URL=$(heroku config:get DATABASE_URL -a whatever_your_app_name_is)
	export DATABASE_URL
