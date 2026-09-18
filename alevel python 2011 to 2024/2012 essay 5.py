datasummary = {}
datakeys = []

def readdata():
	global datakeys, datasummary
	f1 = open('input.txt','r')
	line = f1.readline()
	while (line):
		data = line.strip().split(",")
		for dataitem in data:
			if dataitem in datasummary:
				datasummary [dataitem] += 1
			else:
				datasummary[dataitem] = 1
			datakeys = datakeys + [dataitem]
		line = f1.readline()
	f1.close()

def processdata():
	global datakeys
	for i in range(len(datakeys) - 1):
		for j in range(i+1, len(datakeys)):
			if(datakeys[i] > datakeys[j]):
				datakeys[i], datakeys[j] = datakeys[j], datakeys [i]

def printdata():
	global datakeys, datasummary
	f2 = open('output.txt', 'w')
	for key in datakeys:
		f2.write('{}-{}\n'.format(key,datasummary[key]))
	f2.close()

readdata()
processdata()
printdata()


#1. What are the data types of the variables 
# datasummary and datakeys in the above program?
#   ___(ans)The variable `datasummary` is a dictionary, and the variable `datakeys` is a list.


#2. Write a Python statement required to insert 
#the program name as a comment at the
#beginning of the above program.
# ___(ans)Program Name: Data Processing Program

# What is the result of execution of the 
# command open('input.txt','r') in the above
#program?
# ___(ans)The result is a file object 
# representing the opened file in read mode.

"""
Describe the main task of each of the 
functions readdata(), printdata() and
processdata() in the above program.

 
# readdata() reads the data from input.txt, 
counts each data item,
and stores the items in datakeys.
# processdata() sorts the items in 
datakeys into ascending order.
# printdata() writes each item and its count to 
output.txt.

"""

