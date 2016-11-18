#!/usr/bin/python

import json, sys, sqlite3

print "Content-Type: text/plain;charset=utf-8"
print

data = sys.stdin.read()
j = json.loads(data)

uname = j['username']
password = j['password']

conn = sqlite3.connect("members.db")

cursor = conn.execute("SELECT * from MEMBERS")

b = False
for row in cursor:
	if row[0] == uname:
		b = True
		if row[1] == password:
			print "success"
		else: print "invalid password"
if not b: print "no such user"

# f = open("user.log", "a")
# f.write(j['name'] + "\n")
# f.close()



conn.close()


# {"username": "test3", "password": "pass1234"}