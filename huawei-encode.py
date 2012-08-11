#!/usr/bin/python

out = ""
bytes_read = open("ctce8_HG232.cfg", "rb").read()
for c1 in bytes_read:
	c2 = ord(c1)
	c3 = c2 * 2
	if c3 > 127 :
		c3 = c3 - 127
	out += chr(c3)

print out
