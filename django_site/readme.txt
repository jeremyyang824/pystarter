django-admin startproject django_site

python3 manage.py startapp polls

python3 manage.py runserver 8080


python3 manage.py makemigrations polls

python3 manage.py sqlmigrate polls 0001

python3 manage.py check

python3 manage.py migrate


# interactive command
python3 manage.py shell

# administration
python3 manage.py createsuperuser

# test
python3 manage.py test polls