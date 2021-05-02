#!/bin/python3
import cgi
import requests


form = cgi.FieldStorage()
c_key = form.getvalue('id')
name = form.getvalue('name')
desc = form.getvalue('description')
url = '{{ create_api_endpoint }}?id='
url = url+c_key + '&name=' + name + '&description=' + desc
res = requests.get(url)

print("Content-Type: text/html")
print()

content = res.content
content = content.decode('ascii')
print(f"<h1><center>{ content } </center></h1>")
