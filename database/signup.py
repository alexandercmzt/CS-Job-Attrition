#!/usr/bin/python

import json
import cgi
import sqlite3
import sys

json = cgi.FieldStorage()

#print('Content-type: text/html\n\n')

print "Content-Type: text/plain;charset=utf-8"
print

if json.getvalue('sponsor') == "y":
	sponsor = 1
else: sponsor = 0
if json.getvalue('port') == "y":
	port = 1
else: port = 0
if json.getvalue('github') == "y":
	github = 1
else: github = 0
if json.getvalue('lnkdin') == "y":
	lnkdin = 1
else: lnkdin = 0

try:
    fileName = "./user.log"
    ref = open(fileName, "a")
    ref.write(json.getvalue('username'))
    ref.write("\n")
    ref.write(json.getvalue('cgpa'))
    ref.write("\n")
    ref.write(json.getvalue('mgpa'))
    ref.write("\n")
    ref.write(json.getvalue('grad'))
    ref.write("\n")
    ref.write(json.getvalue('school'))
    ref.write("\n")
    ref.write(json.getvalue('major'))
    ref.write("\n")
    ref.write(json.getvalue('interns'))
    ref.write("\n")
    ref.write(json.getvalue('educ'))
    ref.write("\n")
    ref.write(str(sponsor))
    ref.write("\n")
    ref.write(str(port))
    ref.write("\n")
    ref.write(str(github))
    ref.write("\n")
    ref.write(str(lnkdin))
    ref.write("\n")
    ref.write(json.getvalue('L1'))
    ref.write("\n")
    ref.write(json.getvalue('L2'))
    ref.write("\n")
    ref.write(json.getvalue('L3'))
    ref.write("\n")
    ref.write(json.getvalue('L4'))
    ref.write("\n")
    ref.write(json.getvalue('L5'))
    ref.write("\n")
    ref.write(json.getvalue('M1'))
    ref.write("\n")
    ref.write(json.getvalue('M2'))
    ref.write("\n")
    ref.write(json.getvalue('M3'))
    ref.write("\n")
    ref.write(json.getvalue('M4'))
    ref.write("\n")
    ref.write(json.getvalue('M5'))
    ref.write("\n")
    ref.write(json.getvalue('S1'))
    ref.write("\n")
    ref.write(json.getvalue('S2'))
    ref.write("\n")
    ref.write(json.getvalue('S3'))
    ref.write("\n")
    ref.write(json.getvalue('S4'))
    ref.write("\n")
    ref.write(json.getvalue('S5'))
    ref.write("\n")
    #conn = sqlite3.connect("database/members.db")
    print "db opened\n"
    #cur = conn.cursor()
    # cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD) VALUES ('usertest','passtest');")
	print "execute"
    #cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD, CGPA, MGPA, GRAD, SCHOOL, MAJOR, SPONSOR, PORT, GITHUB, LNKDIN, INTERNS, EDUC, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (name, passwd, cgpa, mgpa, grad, school, major, sponsor, port, github, lnkdin, interns, educ, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5))
    #cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD) VALUES (?, ?);", (json.getvalue('username'), json.getvalue('password')))
	#cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD, CGPA, MGPA, GRAD, SCHOOL, MAJOR, SPONSOR, PORT, GITHUB, LNKDIN, INTERNS, EDUC, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (json.getvalue('username'), json.getvalue('password'), float(json.getvalue('cgpa')), float(json.getvalue('mgpa')), int(json.getvalue('grad')), json.getvalue('school'), json.getvalue('major'), sponsor, port, github, lnkdin, int(json.getvalue('interns')), json.getvalue('educ'), int(json.getvalue('L1')), int(json.getvalue('L2')), int(json.getvalue('L3')), int(json.getvalue('L4')), int(json.getvalue('L5')), int(json.getvalue('M1')), int(json.getvalue('M2')), int(json.getvalue('M3')), int(json.getvalue('M4')), int(json.getvalue('M5')), int(json.getvalue('S1')), int(json.getvalue('S2')), int(json.getvalue('S3')), int(json.getvalue('S4')), int(json.getvalue('S5'))))
	#conn.commit()
    print "success"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
ref.close()
#conn.close()
