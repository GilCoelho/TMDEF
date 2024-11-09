# Tips

## Commands

### Create venv

```cmd
python3 -m venv tmdev_venv
```

### Enter vnev

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
