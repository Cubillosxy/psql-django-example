 ## Requirements
 - python 3
 - postgresql

 ## Get started

 - install postgres
 - Ubunto 16
 `sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib -y`
 #### create db
  1. `sudo su - postgres`
  2. `psql`
  3. `CREATE DATABASE trafilea;`
  4. `CREATE USER django WITH PASSWORD 'django2';`
  5. `GRANT ALL PRIVILEGES ON DATABASE trafilea TO django;`

 #### create virtualenv
 * run :` pip install -r requirements.txt` 

 # Run project
 - `python manage.py migrate`
 - `python mange.py runserver 0.0.0.0:8000`

 the projects is running at *localhost:8000*
 admin site in *localhost:8000/admin*
 admin user : **username = admin , password = admin**
 
 ## Notes
 > Password for users is equal to reverse username.

 
 ## End point
 - http://localhost:8000/users/
 
 ### Test case
 ``` [python]
 import requests
 url = "http://localhost:8000/users/"
 auth = ('example2','2elpmaxe')
 headers_ok = {"apikey": ""}
 headers_bad = {"apikey": "noapi"}
 
 //response ok
 resp = request.get(url, auth=auth, headers=headers_ok)
 print(resp.text)
 
 //response 401
 resp = request.get(url, auth=auth, headers=headers_bad)
 print(resp.status_code)
 
 //no auth 
 resp = request.get(url, headers=headers_bad)
 print(resp.status_code)

 ```
