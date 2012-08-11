#!/usr/bin/python

out = ""
bytes_read = open("ctce8_HG232.cfg", "rb").read()
for c1 in bytes_read:
	c2 = ord(c1)
	if (c2 % 2) == 0 :
		c3 = c2 / 2
	else:
		c3 = ( c2 + 127 ) / 2
	out += chr(c3)

print out

#function jiemi(str) 
#    len1 = len(str)
#    out = ""
#    for i=1 to len1
#        c1 = right(left(str,i),1)
#        c2 = asc(c1)
#        if c2 mod 2=0 then
#            c3 = c2/2
#        else
#            c3 = (c2+127)/2
#        end if
#        out = out & Chr(c3)
#    next
#    f.output.value=out

