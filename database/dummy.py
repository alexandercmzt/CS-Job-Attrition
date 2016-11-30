#!/usr/bin/python
with open('dum.log', 'r') as f:
	html = f.read()

print "Content-Type: text/plain;charset=utf-8"
print
print html