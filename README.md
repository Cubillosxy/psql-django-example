<p align="center">
  <a href="https://opensource.org/licenses/MIT" alt="License: MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square"/>
  </a>
</p>

---
# Posgresql - Django


 ## Requirements
 - python 3
 - postgresql
 ## Get started
 - clone repositorie : `git clone https://github.com/Cubillosxy/psql-django-example.git`
 - install postgres
   * Ubunto 16
   `sudo apt-get install python-dev libpq-dev postgresql postgresql-contrib -y`
   * Mac Os Sierra
   1. `brew install postgresql`
   2. `brew cleanup postgresql`
 #### create db
  1. `sudo su - postgres`
  2. `psql`
  3. `CREATE DATABASE trafilea;`
  4. `CREATE USER django WITH PASSWORD 'django2';`
  5. `GRANT ALL PRIVILEGES ON DATABASE trafilea TO django;`
  6. `ALTER USER django CREATEDB;`

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
 #### Generate apikey
 - sign = "username-Trafilea-email" 
 - apikey = "trafilea" + md5(sign)
 ##### Example
 * username = example2 , email = example2@example.com 
 * sing = "example2-Trafilea-example2@example.com" 
 * apikey = trafileabfa66a4ea7483ebf40aa731205b88cd7
 
 ## End point
 - http://localhost:8000/users/
 
 ### Test case
 ``` [python]
 import requests
 url = "http://localhost:8000/users/"
 auth = ('example2','2elpmaxe')
 headers_ok = {"apikey": "trafileabfa66a4ea7483ebf40aa731205b88cd7"}
 headers_bad = {"apikey": "noapi"}
 
 ##response ok
 resp = requests.get(url, auth=auth, headers=headers_ok)
 print(resp.status_code)
 
 ##response 401
 resp = requests.get(url, auth=auth, headers=headers_bad)
 print(resp.status_code)
 
 ##no auth 
 resp = requests.get(url, headers=headers_bad)
 print(resp.status_code)

 ```
