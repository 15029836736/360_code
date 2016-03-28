#!/usr/bin/env python
import shelve

def dealstr(line):
    line=line.strip()
    str=""
    for i in line:
        if i!=" ":
            str+=i
    return str
while 1:
	print("input one,demo: key=value")
	line=raw_input()
	if line!="q":
		str=dealstr(line)
		index=str.find("=")
		if index!=-1:
		    if str[0].isdigit()==True:
		        key="_"+str[0:index]
		    else:
		        key=str[0:index]
		    value=str[index+1:]
		    db=shelve.open("serverdb")
       		    db[key]=value
        	    db.close()
		else:
		    print("	input error")
		    continue
	else:
		print("		exit ")
		break
