#!/bin/python3
import requests
import cgi

form = cgi.FieldStorage()
c_key = form.getvalue('id')
url = '{{ search_api_endpoint }}?id='

url = url+c_key
res = requests.get(url)

print("Content-Type: text/html")
print()
print(res.json())