# challange
test task for django junior

### For starting project just copy following commands into your terminal:


#### Let's start with virtual environment
  ```
  python3 -m venv env3
  source env3/bin/activate
  ```

#### Install requirements
  ```
  pip install -r requirements.txt
  ```
  
#### Settings
  Create new file `local_settings.py` in `/studsite/students` directory like:
    
    ```
    
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'local_db.sqlite3'),
        }
    }
    ```
    
#### Migrations
  Go to the `studsite` directory and execute following commands:
  ```
  ./manage.py makemigrations students
  ./manage.py migrate 
  ```
  
#### Create superuser for using admin
  Execute following command:
  ```
  ./manage.py createsuperuser
  ```
  Then you will must answer on some questions.

#### Run server
  Afrter user have been created you can run the server and go to the admin page `localhost:8000/admin`.
  Execute this command for running server:
  ```
  ./manage.py runserver
  ```
