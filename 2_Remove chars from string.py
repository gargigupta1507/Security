#!/usr/bin/python2.7

#for a given string remove certain characters from it

def removechar(mystr, delchr):

	output = ""

	for letter in mystr:
		if letter != delchr:
			output += letter

	return output

print(removechar("output", "o"))