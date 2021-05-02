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

content = res.content
content = content.decode('ascii').split(",")

if 'valid' not in content[0]:
    print(f"<h1><center>Id: { content[0] } </center></h1>")
    print(f"<h1><center>Name: { content[1] } </center></h1>")
    print(f"<h3><center>Description: { content[2] } </center></h3>")
else:
    print(f"<h1><center>{ content[0] } </center></h1>")
