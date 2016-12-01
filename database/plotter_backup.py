#!/usr/local/bin/python
import sqlite3
from pprint import pprint
import matplotlib.pyplot as plt, mpld3
import numpy as np
import sys, json, cgi


conn = sqlite3.connect("members.db")

def get_columns(col_name, y_cols):
	cols = []
	cursor = conn.execute("SELECT " +col_name+ " from MEMBERS")
	cols.append([x[0] for x in cursor.fetchall()])
	for col_name in y_cols:
		cursor = conn.execute("SELECT " +col_name+ " from MEMBERS")
		cols.append([x[0] for x in cursor.fetchall()])	
	return np.asarray(cols).T

def numerical_plot(x_var, y_var, scatter = False, school_filter = ""):
	#Getting the data and formatting it
	if y_var == "large":
		matrix = get_columns(x_var, ["L1", "L2", "L3", "L4", "L5", "SCHOOL"])
	elif y_var == "medium":
		matrix = get_columns(x_var, ["M1", "M2", "M3", "M4", "M5", "SCHOOL"])
	else:
		matrix = get_columns(x_var, ["S1", "S2", "S3", "S4", "S5", "SCHOOL"])

	if school_filter != "":
		matrix =  matrix.tolist()
		matrix = np.array([row for row in matrix if row[0] != None and row[1] != None and row[1] != 0.0]).T
		matrix = matrix.T.tolist()
		matrix = np.array([row[:-1] for row in matrix if row[-1] == school_filter]).T.astype(np.float32)
	else:
		matrix =  matrix.tolist()
		matrix = np.array([row[:-1] for row in matrix if row[0] != None and row[1] != None and row[1] != 0.0]).T.astype(np.float32)
	#Setting up the plot environment
	fig = plt.figure()
	fig.set_size_inches(20,10)
	ax = fig.add_subplot(111)
	plt.ylabel("Stage reached as percentage of total companies applied to")
	plt.xlabel(x_var)
	axes = plt.gca()
	axes.set_ylim([0,100])
	if x_var in ['MGPA', 'CGPA']:
		axes.set_xlim([2.5,4])

	#Plotting the data
	if scatter:
		ax.plot(matrix[0],100*matrix[2]/matrix[1], 'ro', label="HR screen/online interview/coding challenge")
		ax.plot(matrix[0],100*matrix[3]/matrix[1], 'yo', label="Remote technical interview")
		ax.plot(matrix[0],100*matrix[4]/matrix[1], 'bo', label="On-site interview")
		ax.plot(matrix[0],100*matrix[5]/matrix[1], 'go', label="Employment Offer")
	else:
		x = matrix[0]
		ax.plot(np.unique(x), np.poly1d(np.polyfit(x, 100*matrix[2]/matrix[1], deg=2))(np.unique(x)), 'r', label="HR screen/online interview/coding challenge")
		ax.plot(np.unique(x), np.poly1d(np.polyfit(x, 100*matrix[3]/matrix[1], deg=2))(np.unique(x)), 'y', label="Remote technical interview")
		ax.plot(np.unique(x), np.poly1d(np.polyfit(x, 100*matrix[4]/matrix[1], deg=2))(np.unique(x)), 'b', label="On-site interview")
		ax.plot(np.unique(x), np.poly1d(np.polyfit(x, 100*matrix[5]/matrix[1], deg=2))(np.unique(x)), 'g', label="Employment Offer")
		ax.plot(matrix[0],100*matrix[2]/matrix[1], 'ro')
		ax.plot(matrix[0],100*matrix[3]/matrix[1], 'yo')
		ax.plot(matrix[0],100*matrix[4]/matrix[1], 'bo')
		ax.plot(matrix[0],100*matrix[5]/matrix[1], 'go')

	return fig
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


def categorical_plot(x_var, y_var, school_filter = ""):
	#Getting the data and formatting it
	if y_var == "large":
		matrix = get_columns(x_var, ["L1", "L2", "L3", "L4", "L5", "SCHOOL"])
	elif y_var == "medium":
		matrix = get_columns(x_var, ["M1", "M2", "M3", "M4", "M5", "SCHOOL"])
	else:
		matrix = get_columns(x_var, ["S1", "S2", "S3", "S4", "S5", "SCHOOL"])

	if school_filter != "":
		matrix =  matrix.tolist()
		matrix = np.array([row for row in matrix if row[0] != None and row[1] != None and row[1] != 0.0]).T
		matrix = matrix.T.tolist()
		matrix = np.array([row[:-1] for row in matrix if row[-1] == school_filter]).T.tolist()
	else:
		matrix =  matrix.tolist()
		matrix = np.array([row[:-1] for row in matrix if row[0] != None and row[1] != None and row[1] != 0.0]).T.tolist()
	for i in xrange(1,len(matrix)):
		matrix[i] = map(float, matrix[i])

	fig, ax = plt.subplots()

	if x_var in ['GITHUB', 'PORT', 'LNKDIN', 'SPONSOR']:
		ymatrix = np.array(matrix).T.tolist()
		ymatrix = np.array([row[1:] for row in ymatrix if row[0] == 1]).T.tolist()
		nmatrix = np.array(matrix).T.tolist()
		nmatrix = np.array([row[1:] for row in nmatrix if row[0] == 0]).T.tolist()
		ymatrix = [sum(col)/float(len(col)) for col in ymatrix]
		nmatrix = [sum(col)/float(len(col)) for col in nmatrix]
		index = np.arange(5)
		bar_width = 0.35
		opacity = 0.4
		rects_yes = plt.bar(index, ymatrix, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Yes')
		rects_no = plt.bar(index+bar_width, nmatrix, bar_width,
                 alpha=opacity,
                 color='r',
                 label='No')
		plt.ylabel('Average count')
		plt.xticks(index + bar_width, ('Applied to', 'Online/HR Screen', 'Remote technical', 'Onsite', 'Offer'))
		plt.legend()
		plt.tight_layout()
	else:
		index = np.arange(5)
		bar_width = 0
		bw = 0.15
		opacity = 0.4
		categories = set(np.array(matrix).tolist()[0])
		colors = "bgrcmykw"
		color_index = 0
		i=0
		for category in categories:
			curr_matrix = np.array(matrix).T.tolist()
			curr_matrix = np.array([row[1:] for row in curr_matrix if row[0] == category]).tolist()
			for i in xrange(len(curr_matrix)):
				curr_matrix[i] = map(float, curr_matrix[i])
			curr_matrix = np.array(curr_matrix).T.tolist()
			curr_matrix = [sum(col)/float(len(col)) for col in curr_matrix]
			rects_curr = plt.bar(index+bar_width, curr_matrix, bw,
                 alpha=opacity,
                 color=colors[color_index],
                 label=category)
			color_index+=1
			bar_width+=bw
		plt.ylabel('Average count')
		plt.xticks(index + len(categories)*bw/2, ('Applied to', 'Online/HR Screen', 'Remote technical', 'Onsite', 'Offer'))
		plt.legend()
		plt.tight_layout()
	return fig

# with open('dum.log', 'w') as f:
# 	f.write(mpld3.fig_to_html(numerical_plot('CGPA', 'large')))
# raw_input()

# json_input = cgi.FieldStorage()


# print "Content-Type: text/plain;charset=utf-8"
# print

# # j = json.loads(data)

# x = json_input.getvalue('xAxis')
# y = json_input.getvalue('yAxis')
# school = json_input.getvalue('schoolFilter')

# if x in ["CGPA", "MGPA", "GRAD", "INTERNS"]:
# 	output_plot = numerical_plot(x, y, school_filter = school)
# else:
# 	output_plot = categorical_plot(x, y, school_filter = school)
# output_json = mpld3.fig_to_html(output_plot)

# print output_json

name = sys.argv[1]

output_plot = numerical_plot(name, 'large', school_filter= "McGill University")
output_json = mpld3.fig_to_html(output_plot)

with open("backup_plots/"+name + "-mcgill.backup", "w") as f:
	f.write(output_json)
f.close()
conn.close()

