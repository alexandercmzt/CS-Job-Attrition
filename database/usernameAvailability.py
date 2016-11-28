#!/usr/bin/python

import json
import cgi
import sqlite3
import sys

json = cgi.FieldStorage()

print('Content-type: text/html\n\n')

try:
    conn = sqlite3.connect("members.db")
    cursor = conn.execute("SELECT * from MEMBERS")
    alreadyExists = False
    for row in cursor:
        if row[0] == json.getvalue('name'):
            alreadyExists = True
            print "username already exists"
    if not alreadyExists: print "username is available"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
conn.close()
