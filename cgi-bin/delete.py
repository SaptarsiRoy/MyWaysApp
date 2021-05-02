#!/bin/python3
import requests
import cgi

form = cgi.FieldStorage()
c_key = form.getvalue('id')
url = '{{ delete_api_endpoint }}?id='

url = url+c_key
res = requests.get(url)

print("Content-Type: text/html")
print()


content = res.content
content = content.decode('ascii')
print(f"<h1><center>{ content } </center></h1>")
