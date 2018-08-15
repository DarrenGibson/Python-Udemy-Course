#=================================================================#
#					   Pyhton Udemy Course
#-----------------------------------------------------------------#

'''
Date		: Tue 14 Aug 2018 04:02:21 PM PDT 
Author		: Darren Gibson
Title		: Python Udemy Course 
Resources	: https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3812186?start=0

'''

# Lec 28 An introduction to program flow control

'''
NOTES:
python works in blocks (indentations) of code, becaus eof this python does not use delimeters.



'''
# notice we must indent print() for it to work
for i in range(1, 12):
	print('no {} squared is {} and cubed is {:4})'.format(i, i**2, i**4))
	
# Lec 29 
	
'''
NOTES:


'''

# we can use ask for input, and then imediatley use that input while also asking for more data
name = input('please enter your name: ')
age = input('how old are you, {}?'.format(name))
# in order to get an integer value we will add the int() to input()
# this will stil error if we type in char vars
age = int(input('how old are you, {}? '.format(name))) #  remember, 3 now
print(age)
# WE ARE CONVERTING THIS STRING INTO AN INTERGER SO THAT WE CAN PERFORM CONDITIONS LIKE IF STATEMENTS AND OTHERS 
if age >=18:
	print('you are old enough to vote')
else:
# we can perform a little bit of math here if we like
	print('please come back when in {} years'.format(18 - age)	



























































