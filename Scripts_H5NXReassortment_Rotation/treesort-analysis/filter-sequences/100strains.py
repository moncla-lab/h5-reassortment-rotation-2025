#! /usr/bin/env/python 

#set the input file name
#(The program must be run from within the directory that contains this data file)
InFileName = "include_strains_h5nx_100.txt"

#Open the input file for reading
InFile = open(InFileName, 'r')

#Initialize the counter used to keep track of line numbers 
LineNumber = 0

OutFileName = "new" + InFileName
OutFile = open(OutFileName, 'w') 

#Loop through each line in the file
for Line in InFile: 
	Line = Line.strip('/n') #remove line ending characters
	ElementList = Line.split('\t')
	OutputString = ElementList[0]
	print(OutputString)
#	print(LineNumber, ':', ElementList)
	OutFile.write(OutputString + "\n")
	LineNumber = LineNumber + 1
	
InFile.close()
OutFile.close()
	