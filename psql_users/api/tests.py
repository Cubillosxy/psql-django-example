from django.test import TestCase

# Create your tests here.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import requests
from psql_users.settings import SIGN_API
import hashlib
from rest_framework.test import APIClient

class ValidateApis(unittest.TestCase):
	def setUp(self):
        self.client = APIClient()
        self.client.login(username='example2',
                          password="2elpmaxe")
        
        sign = "%s-%s-%s" % (username, SIGN_API, email)
        apikey = "trafilea" + hashlib.md5(sign.encode('utf-8')).hexdigest()
        self.headers.ok = {"apikey": }
		self.headers_bad= { "apikey" : "asdasfd" }
		self.url = "http://localhost:8000/users/"


	def test_apikey_error(self):
		print("validate apikey  ... ")
        response = self.client.get(self.url, headers=self.headers_bad)
		print (response.text)
		self.assertEqual(response.status_code, 401)
		print("end test_apikey_error")

	def test_api_response(self):
		print("validate api response  ... ")
		response = self.client.get(self.url, headers=self.headers_ok)
		self.assertEqual(response.status_code, 200)
		print("end test_apikey_error")