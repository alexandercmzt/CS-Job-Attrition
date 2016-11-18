#!/usr/bin/python
import json, sys
print "Content-Type: text/plain;charset=utf-8"
print
data = sys.stdin.read()
j = json.loads(data)
f = open("user.log", "a")
f.write(j['name'] + "\n")
f.close()
