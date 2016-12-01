#!/usr/bin/python

import json
import cgi
import sqlite3
import sys

json = cgi.FieldStorage()

print "Content-Type: text/plain;charset=utf-8"
print

x=json.getvalue('xAxis')
s=json.getvalue('filterSchool')

if "McGill" in s:
	filename = "backup_plots/" + x + "-mcgill.backup"
else:
	filename = "backup_plots/" + x + ".backup"

with open(filename, 'r') as f:
	html = f.read()

print html