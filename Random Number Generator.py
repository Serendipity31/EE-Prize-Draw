# This is a random number generator. First use is determining who gets the prizes for the alumni survey.

# First step is to import the matrix of respondents who are eligible into programme
# Tried to follow basics from here: http://stackoverflow.com/questions/10937918/loading-a-file-into-a-numpy-array-with-python 

import csv
import random 
import os

print "The current working directory is", os.getcwd()
os.chdir(r'G:\CKD BAULCOMB\MSc Involvement')
print "The new working directory is", os.getcwd()

while True:
	print("Welcome to Corinne's Prize Drawing Programme")
	N = raw_input("How many prizes do you want to offer? ")
	
	F = raw_input(
	"Please enter the file path for the .csv file containing the eligible respondents. \
	Be sure to remove any headers from this file before uploading it here: ")
	# G:\CKD BAULCOMB\MSc Involvement\STSurveyResults_Prize Draw.csv

	O = raw_input(
	"Please enter the file path you would like for the results file: ")
	# G:\CKD BAULCOMB\MSc Involvement\STSurvey_winners.txt

	ERfile = open(F, 'rb')
	# Old version: open(r'G:\CKD BAULCOMB\MSc Involvement\Study Tour Survey Results_22 September_Prize Draw.csv', 'rb')
	# the r here is the rawstring marker and it means I don't have to 'escape' every instance of the \
	# Alternatives are to use / instead or to 'escape' each instance by using \\
	# When have user input file path, it automatically 'escapes' that file path, so this is not needed

	ERdata = csv.reader(ERfile, delimiter=',')
	ERtable = [row for row in ERdata]
	# at this point it should read like a matrix - should be able to call entries based on row and column information

	Winners = random.sample(ERtable, 5)
	# select the people who will get the prize

	Places = range(1, int(N)+1)
	# Designates winner places 1 - 5
	
	Results = open(O, 'w')

	for x in Places: 
		print 'Winner %d is...%s' %(x, Winners[x-1])
		print >>Results, 'Winner %d is...%s' %(x, Winners[x-1])
		# helpful: http://learnpythonthehardway.org/book/ex32.html 
	
	Results.close()

	Answer = raw_input("Run again? (y/n): ")
	if Answer == 'n':
		print("Goodbye")
		False
		break
	else:
		continue

#Points for improvement
# 1. Putting in if/then statements to ensure answers are given in the correct format
# 2. Enable change of file path/directories on each iteration 
# 3. Add counter to file names so don't have to specify each time