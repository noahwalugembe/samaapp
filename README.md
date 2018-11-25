# README #

**Setup Instructions**

  Clone repo

  ```
  $ git clone https://github.com/noahwalugembe/samaapp.git
  ```

  Install [pipenv](https://pypi.org/project/pipenv/)
  ```
  $ pipenv install 
  ```
  
  Activate virtualenv  
  ```
  $ pipenv run
  ```

  Migrate
  ```
  $ python manage.py migrate
  ```
  
  Run app
  ```
  $ python manage.py runserver
  ```
  
  To change data base to postgresql
  
  Find this part in your mysite/settings.py file:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
And replace it with this:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangogirls',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
Remember to change name to the user name that you created earlier in this chapter.