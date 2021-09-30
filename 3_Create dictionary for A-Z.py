#!/usr/bin/python2.7

#create dictionary from file

file = open("3_input.csv", "r")

mydiction = {}

def createdict():
	line = file.readline()
	while line != "":
		for i in line:
			if (ord(i) > 64 and ord(i) < 91):
				if i not in mydiction.keys():
					mydiction[i] = 1
				else:
					mydiction[i] += 1
		line = file.readline()

	return mydiction


print(createdict())