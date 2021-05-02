#!/bin/python3
import  cgi
import requests


form = cgi.FieldStorage()
c_key = form.getvalue('id')
error = False
content = None
lower_alpha_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
upper_alpha_list = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
for i in c_key:
    if i in lower_alpha_list or i in upper_alpha_list:
        error = True
        break

if not error:
    name = form.getvalue('name')
    desc = form.getvalue('description')
    url = '{{ create_api_endpoint }}?id='

    url = url+c_key + '&name=' + name + '&description=' + desc
    res = requests.get(url)
    content = res.content
    content = content.decode('ascii')
else:
    content = "Enter Valid Candidate ID"

print("Content-Type: text/html")
print()


print(f"<h1><center>{ content } </center></h1>")