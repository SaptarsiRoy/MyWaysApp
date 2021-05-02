#!/bin/python3
import requests
import cgi

form = cgi.FieldStorage()
c_key = form.getvalue('id')
url = 'https://9651321x46.execute-api.ap-south-1.amazonaws.com/default/MyWays-delete?id='

url = url+c_key
res = requests.get(url)

print("Content-Type: text/html")
print()


content = res.content
content = content.decode('ascii')
print(f"<h1><center>{ content } </center></h1>")
