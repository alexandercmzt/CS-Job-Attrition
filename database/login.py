#!/usr/bin/python

import json
import cgi
import sqlite3
import sys

json = cgi.FieldStorage()

#print('Content-type: text/html\n\n')

print "Content-Type: text/plain;charset=utf-8"
print

try:
    conn = sqlite3.connect("members.db")
    cursor = conn.execute("SELECT * from MEMBERS")
    b = False
    for row in cursor:
        if row[0] == json.getvalue('name'):
            b = True
            if row[1] == json.getvalue('pwd'):
                print "success"
            else: print "wrong password"
    if not b: print "no such user"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
conn.close()
