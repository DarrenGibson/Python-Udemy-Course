#==================================================================
#						Break challange
#==================================================================

''' 
Date    : Fri 17 Aug 2018 10:40:41 PM PDT 
Subject : Break challange
Title   : Break challange
Source  : https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/quiz/4428944
''' 

#

'''
NOTES:

'''

# this is the answer given by the udemy
for i in range(0, 100, 7):
	print(i)
	if i > 0 and i % 11 == 0:
		break
		
# but i was wondering if this might actually work
for i in range(0, 100, 7):
	print(i)
	if i/7 == 11:
		break
# IT DID NOT WORK
# hahahhahah actually it did once i changed the % into a / like it is supposed to be


	
	





















































































