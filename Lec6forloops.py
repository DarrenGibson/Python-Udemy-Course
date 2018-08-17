
#=================================================================#
#			    Pyhton Section 6 Lecture 33 for loops
#-----------------------------------------------------------------#

'''
Date		: Fri 17 Aug 2018 12:45:56 PM PDT 
Author		: Darren Gibson
Title		: Section 6: Lec 33 - for loops
Resources	: https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3829344?start=75
'''

# Lec 33 - for loops

'''
NOTES:


'''

# we can have our code repeat itself for a specified amount of time 
# the number 20 will not be displayed, only up to 19
# loop control variables i and j are acceptable variable names
for i in range(1, 20):
	print('i is now {}'.format(i))
# I had this error because i did not add the last paranthesis
'''
 File "Lec6forloops.py", line 43
    
    ^
'''

# we can display individual characters with a for loop 
num1 = '9,223,372,036,854,775,807'
for i in range(0, len(num1)):
	print(num1[i])
# because i had paranthesis around [i] , i recieved this error
'''
  File "Lec6forloops.py", line 35, in <module>
    print(num1([i]))
TypeError: 'str' object is not callable
'''
	
# this is one way elininate the seperators 
num2 = '9,223,372,036,854,775,807'
for i in range(0, len(num2)):
	if num2[i] in '01234556789':
# by default the print() is set to include a new line everytime it is used 
		print(num2[i], end='')
# but we are able to keep them all on the same line with 
# print(num2[i], end='')

# if we want to use the number created to perform calculations we can do 
# by concatinating each char onto the new string and then convert the final 
# thing into an integer.


num3 = '9,223,372,036,854,775,807'
cleanedNumber = ''
for i in range(0, len(num3)):
	if num3[i] in '0123456789':
		cleanedNumber = cleanedNumber + num3[i]
		print(num3[i], end='')
		
# I tried to add these comments after line 61 but it keept saying 
'''
    \'\'\'
      ^
IndentationError: expected an indented block

'''
# This is because the line before then ends with cleanedNumber = ''

# forgot to add the : here and recieved this error message
'''
    for i in range(0, len(num3))
                               ^
SyntaxError: invalid syntax
'''

# the complete version of the above program
num4 = '9,223,372,036,854,775,807'
cleanedNumber = ''
for i in range(0, len(num4)):
	if num4[i] in '0123456789':
		cleanedNumber = cleanedNumber + num4[i]
newNumber = int(cleanedNumber)
print('the number is {}'.format(newNumber))























