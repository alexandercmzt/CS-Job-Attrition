#!/usr/bin/python
import sqlite3, json, random

f = open("USandCANunis.json", "r")
schools = json.load(f)
n = len(schools)
majors = ["Computer Science", "Software Engineering"]
others = ["Computer Engineering", "Engineering (Other)", "Non-Engineering program"]



conn = sqlite3.connect("members.db")

for i in range(0, 501):
	rand = random.randrange(n-1)
	school = schools[rand]
	name = "user" + str(i)
	passwd = "pass" + str(i)
	cgpa = round(random.uniform(2.50, 4.00), 2)
	mgpa = cgpa + round(random.uniform(0.00, 0.30), 2)
	grad = random.randrange(0, 7)
	sponsor = random.randrange(0, 2)
	port = random.randrange(0, 2)
	github = random.randrange(0, 2)
	lnkdin = random.randrange(0, 2)
	interns = random.randrange(0, 6)
	if i < 400:
		educ = "Bachelors"
		major = random.choice(majors)
	elif i < 450:
		educ = "Masters"
		major = random.choice(others)
	else:
		educ = "PhD"
		major = random.choice(others)
	if cgpa > 3.8:
		x, y, z = 4, 3, 2
	elif cgpa > 3.3:
		x, y, z = 3, 3, 2
	else:
		x, y, z = 0, 0, 0
	m = random.randrange(10, 30)
	l = range(m)
	L1 = random.choice(l[x:])
	L2 = random.choice(l[x:L1+1])
	L3 = random.choice(l[x:L2+1])
	L4 = random.choice(l[x:L3+1])
	L5 = random.choice(l[x:L4+1])
	M1 = random.choice(l[y:])
	M2 = random.choice(l[y:M1+1]) 
	M3 = random.choice(l[y:M2+1])
	M4 = random.choice(l[y:M3+1])
	M5 = random.choice(l[y:M4+1])
	S1 = random.choice(l[z:]) 
	S2 = random.choice(l[z:S1+1])
	S3 = random.choice(l[z:S2+1])
	S4 = random.choice(l[z:S3+1])
	S5 = random.choice(l[z:S4+1])

	#print name, passwd, cgpa, mgpa, grad, school, major, sponsor, port, github, lnkdin, interns, educ, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5

	cur = conn.cursor()

	cur.execute("INSERT INTO MEMBERS (UNAME, PASSWD, CGPA, MGPA, GRAD, SCHOOL, MAJOR, SPONSOR, PORT, GITHUB, LNKDIN, INTERNS, EDUC, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5)"
		" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
		(name, passwd, cgpa, mgpa, grad, school, major, sponsor, port, github, lnkdin, interns, educ, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5))

	conn.commit()

conn.close()