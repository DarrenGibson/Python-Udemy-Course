#==================================================================
#			            augmented assignment
#==================================================================

''' 
Date    : Thu 06 Sep 2018 12:42:32 PM PDT 
Subject : Udemy / Practice 
Title   : program flow
Source  : https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/6135262?start=690
''' 

#

'''
NOTES:

'''

ipAddress = input('please enter an address: ')

segment = 1
length = 0        	# len is not a good var name becaue
					# it shadows the len command
for character in inAddress:
	if character == '.':
		print('segment {} contains {} characters'.format(segment, length))
		segment +=1
		length = 0
		
	else:
		length +=1


















































































