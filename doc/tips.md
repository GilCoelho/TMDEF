# Tips

## Commands

### Create venv

```cmd
python3 -m venv tmdev_venv
```

### Enter venv

```cmd
source tmdev_venv/bin/activate
```

### Install requirements

```cmd
pip install -r requirements.txt
```

## Django

### Create Django project

```cmd
django-admin startproject TMDEV
```

### Start Django project

```cmd
python3 manage.py runserver
```

### Create a new app inside previous project

```cmd
cd TMDEV
python3 manage.py startapp Forms
```

### Update db after change Models

```cmd
python3 manage.py makemigrations Forms
python3 manage.py migrate
```

### Update app

Every time that a new app is created inside the project, the follow command shall be run:

```cmd
python3 manage.py migrate
```

### Set data to DB before start Server

Check [link](https://docs.djangoproject.com/en/5.1/howto/initial-data/)

```cmd
python3 manage.py loaddata <fixturename>
```

Note: This can only be run after the *db* already contains the Table

### Delete DB locally

1. Delete the sqlite database file (often db.sqlite3) in your django project folder (or wherever you placed it)
2. Delete everything except __init__.py file from migration folder in *all* django apps

    ```cmd
    rm */migrations/0*.py
    ```

3. Make changes in your models (models.py).
4. Run the command python:

    ```cmd
    python3 manage.py makemigrations
    ```

5. Then run the command python manage.py migrate.

### Useful Commands

```cmd
find .. | grep -E 'migrations/0.*py' | grep -v '.*_venv.*' | xargs rm
find .. | grep -E 'db.sqlite3' | grep -v '.*_venv.*' | xargs rm

python3 manage.py makemigrations
python3 manage.py migrate

find .. | grep -E 'fixtures/.*json' | xargs python3 manage.py loaddata

python3 manage.py runserver
```
