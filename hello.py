#!/usr/bin/env python3
import os
import cgi
import cgitb
import json
from templates import login_page
import secret

cgitb.enable()

environ_dict = dict(os.environ)
environ_json = json.dumps(environ_dict)

print("Content-Type: text/html")
print()

print(environ_json + "<br/>")
if "QUERY_STRING" in environ_dict:
    print("<br/>Query String: " + environ_dict["QUERY_STRING"])
if "HTTP_USER_AGENT" in environ_dict:
    print("<br/>User Browser Information: " + environ_dict["HTTP_USER_AGENT"])
print("<br/>Form Data: " + str(cgi.FieldStorage()))  
# print(cgi.FieldStorage()["username"])
print("<br/")

print(login_page())