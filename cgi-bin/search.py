#!/bin/python3
import requests
import cgi

form = cgi.FieldStorage()
c_key = form.getvalue('id')
url = 'https://9651321x46.execute-api.ap-south-1.amazonaws.com/default/MyWays-search?id='

url = url+c_key
res = requests.get(url)

print("Content-Type: text/html")
print()
print(res.json())