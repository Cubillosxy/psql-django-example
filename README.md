# psql-django-example
Web service for get users data

# Requirements
-python 3
-postgresql 

# Get started

-install postgres
-for Ubunto run 
sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib -y
-create a db 
 -sudo su - postgres
 -psql
 -CREATE DATABASE trafilea;
 -CREATE USER django WITH PASSWORD 'django2';
 -GRANT ALL PRIVILEGES ON DATABASE trafilea TO django;

-create virtualenv 
-run : pip install -r requirements.txt

# Run project
-python manage.py migrate
-python mange.py runserver 0.0.0.0:8000

the projects is running at localhost:8000 
admin site in localhost:8000/admin   
admin user : username = admin , password = admin
