#!/usr/bin/python
import sqlite3

print "hello"

conn = sqlite3.connect("members.db")
print "db opened\n"

# conn.execute('''CREATE TABLE MEMBERS
#  		(UNAME TEXT PRIMARY KEY NOT NULL,
#  		PASSWD TEXT NOT NULL,
#  		CGPA REAL,
#  		MGPA REAL,
#  		GRAD INT,
#  		SCHOOL TEXT,
#  		MAJOR TEXT,
#  		SPONSOR INT,
#  		PORT INT,
#  		GITHUB INT,
#  		LNKDIN INT,
#  		INTERNS INT,
#  		EDUC TEXT,
#  		L1 INT,
#  		L2 INT,
#  		L3 INT,
#  		L4 INT,
#  		L5 INT,
#  		M1 INT,
#  		M2 INT,
#  		M3 INT,
#  		M4 INT,
#  		M5 INT,
#  		S1 INT,
#  		S2 INT,
#  		S3 INT,
#  		S4 INT,
#  		S5 INT);''')


# conn.execute("INSERT INTO MEMBERS (UNAME, PASSWD) VALUES ('testing', 'password1234')");
# conn.commit()

# conn.execute("INSERT INTO MEMBERS (UNAME, PASSWD, CGPA, MGPA, GRAD, SCHOOL, MAJOR, SPONSOR, PORT, GITHUB, LNKDIN, INTERNS, EDUC, L1, L2, L3, L4, L5, M1, M2, M3, M4, M5, S1, S2, S3, S4, S5)"
# 	"VALUES ('bob', 'pass123', 3.04, 3.45, 3, 'McGill University', 'Software Engineering', 1, 1, 0, 0, 2, 'Bachelors', 5, 2, 1, 0, 0, 7, 3, 2, 1, 1, 12, 5, 4, 1, 1)");
# conn.commit()


# conn.execute("DELETE FROM MEMBERS WHERE UNAME='testing';")
# conn.commit()

cursor = conn.execute("SELECT * from MEMBERS WHERE MAJOR='Non-Engineering program'")
print cursor.fetchall()
# for row in cursor:
# 	for i in range(len(row)):
# 		if row[i] is not None:
# 			print row[i]
# 	print


conn.close()