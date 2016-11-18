#!/usr/bin/python

import json, sys, sqlite3

print "Content-Type: text/plain;charset=utf-8"
print

#data = sys.stdin.read()

data = '{"username": "bill", "password": "pass1234", "cgpa": "3.94", "mgpa": "3.81", "grad": "3", "school": "McGill University", "major": "Computer Engineering", "sponsor": "yes", "port": "no", "github": "yes", "lnkdin": "no", "interns": "2", "educ": "Bachelors", "L1": "4", "L2": 3, "L3": 1, "L4": 1, "L5": 0, "M1": 12, "M2": 9, "M3": 2, "M4": 1, "M5": 1, "S1": 6, "S2": 4, "S3": 4, "S4": 3, "S5": 2}'

j = json.loads(data)

if j['sponsor'] == "y":
	j['sponsor'] = 1
else: j['sponsor'] = 0
if j['port'] == "y":
	j['port'] = 1
else: j['port'] = 0
if j['github'] == "y":
	j['github'] = 1
else: j['github'] = 0
if j['lnkdin'] == "y":
	j['lnkdin'] = 1
else: j['lnkdin'] = 0


conn = sqlite3.connect("members.db")

cursor = conn.execute("SELECT * from MEMBERS WHERE UNAME=(?);", [j['username']])
if len(cursor.fetchall()) > 0:
	print "username taken"

else:
	cur = conn.cursor()
	cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD, CGPA, MGPA, GRAD, SCHOOL, MAJOR, SPONSOR, PORT, GITHUB, LNKDIN, INTERNS, EDUC, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5)"
		" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", 
		(j['username'], j['password'], j['cgpa'], j['mgpa'], j['grad'], j['school'], j['major'], j['sponsor'], j['port'], j['github'], j['lnkdin'], j['interns'], j['educ'], 
			j['L1'], j['L2'], j['L3'], j['L4'], j['L5'], j['M1'], j['M2'], j['M3'], j['M4'], j['M5'], j['S1'], j['S2'], j['S3'], j['S4'], j['S5']))
	conn.commit()
	print "success"

 
# f = open("user.log", "a")
# f.write(j['name'] + "\n")
# f.close()

 #{"username": "test3", "password": "pass1234", "cgpa": 2.68, "mgpa": 3.02, "grad": 5, "school": "UBC", "major": "Computer Science", "sponsor": 1, "port": 0, "github": 0, "lnkdin", 1, "educ": "Bachelors", "L1": 32, "L2": 2, "L3": 2, "L4": 1, "L5": 0, "M1": 16, "M2": 2, "M3": 0, "M4":0, "M5": 0, "S1": 13, "S2": 6, "S3": 4, "S4": 2, "S5": 1}



conn.close()

