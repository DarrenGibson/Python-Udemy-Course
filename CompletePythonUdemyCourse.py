#=================================================================#
#					   Pyhton Udemy Course
#-----------------------------------------------------------------#

'''
Date		: Mon 13 Aug 2018 02:00:19 PM PDT 
Author		: Darren Gibson
Title		: Python Udemy Course 
Resources	: www.udemy/python-the-complete-python-developer-course
'''

'''                     The basics of python                    '''



# Lec 23 output

'''	
NOTES:
object oriented interpretted language. 
Python 2.7 will be the last version of pyhton2
'''

# first program 
print('hello hello')

# print function can perform math and display resluts
print(1+2)
print(7*6)
print()
print('the end')

# we use double quotes when we need to use an apostrophy in out sentence
print("python's strings are easy to use")
print('we can even include "quotes" in strings')
print('and if that don\'t help than we can use an escape character')

# concatinating strings
print('hello' + ' world')

# concatinating variable strings
greeting = 'hello'
name = 'darren'
print(greeting + name)
print(greeting + ' ' + name)

					  

# lec 24 input
''' 		
NOTES:

'''

# using the input() function to get data from the user
greeting = 'hello'
name = input('what is your name: ')
print(greeting + ' ' + name)

# using a new line escape character to creat a new line
splitString = 'This string has been\nsplit over\nseveral \nlines'
print(splitString)

# using tabbed escape characters
tabbedString = '1\t2\t3\t4\t5\t'
print(tabbedString)

# here is a creative example of 
print('the petshop owner said "no, no \'e\'s uh,...he\s resting"')
print("the petshop owner said \"no, no, 'e's uh,...he's resting\"")

# using multiline comments to split up a sentance string
anotherSplitString = """this string has been
split over
several lines"""
print(anotherSplitString)




# lec 25 variables
'''
NOTES:
floating point numbers have a little over 300 digits high and low
floating point numbers have 52 digits of precision
programs operate faster without floating point number
real numbers are numbers with a fractional amount
complex numbers ???
strings are a sequence type
variable numes, cannot start with a number.  can start with an under score
'''

# several variable names
greeting = 'darren '
_myName = 'tim '
Time45 = 'good '
Greeting = 'day '
print(greeting + _myName + Time45 + Greeting)

# concatinating strings and integers
# age = 36
# print(greeting + age) 
# this will cause an error, we actually need to convert this to
# tried this, didn't work
# age = str(age) 
# print(greeting + age)    ?????

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)	# This returns a floating point number
print(a // b)	# This returns an integer
print(a % b)	# This returns the remainder after the quotaint

'''
# short example of how not using the correct equassion 
for i in range(1, a/b): # replace a/b with 4, works and // does
	print(i)
	
	
  File "CompletePythonUdemyCourse.py", line 118, in <module>
    for i in range(1, a/b): # replace a/b with 4 works
TypeError: 'float' object cannot be interpreted as an integer
'''

# of course the rules of operation still apply
print(a + b / 3 -4 * 12)
# all of them
print((a + b) / 3 -4 * 12)



# lec 26 variables and strings continued
'''
NOTES:


'''
# we can replacate the formula above with variables
c = a + b
d = c / 3
e = d - 4
print(e *12)

# how to retreave index's 
parrot = 'norwegian blue'
print(parrot)
print(parrot[0])
print(parrot[3])
# print(parrot[34]) # will error
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])

# we can use this simple technique to remove the commas
number = '9,223,372,036,854,775,807'
print(number[1::4])

# better method
numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9'
print(numbers[0::3])

# concatinating more strings
string1 = 'he\'s '
string2 = 'probably '
print(string1 + string2)
print('he\'s probably home')

# multiplication with strings
'''
print('hello' * 5)
print('hello' * 5 + 4)

  File "CompletePythonUdemyCourse.py", line 176, in <module>
    print('hello' * 5 + 4)
TypeError: must be str, not int
'''
# only works this way
print('text' * (5 + 4))
print('text' * 5 + '4')

# returns true or false if a string is located in anoter string
today = 'friday'
print('day' in today)
print('fri' in today)
print('thur' in today)
print('parrot' in 'fjord')




# lec 27 string formatting
'''
NOTES:
# the f in %12.50f is important ?!?!  code will not run without it, why???

'''
# replacement fields are the way to go
# well look at this for a second time.  shows error
age = 24
# print('my age is ' + 24 '')
# to translate this into good code we 
print('my age is ' + str(age) + ' years')

# output string with .format() 
print('my age is {} years old'.format(age))

# .format Exagurated 
print('there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}'.format(31, 'January', 'March', 'May',
'July', 'August', 'October', 'December'))

# output with triple quotes and multiple replacement values
print('''January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
Novermber: {1}
December: {2}'''.format(28, 30, 31))

# old process python 2 method
print('my age is %d years' % age)
print('my age is %d %s, %d %s' % (age, 'years', 6, 'months'))

# a loop that uses python 2 formating methods
for i in range(1, 12):
# theses numbers after % indicate spaceing
	print('no, %2d squared is %4d and cubed is %4d' %(i, i ** 2, i ** 3))

# we can also get the percision of a number by
print('Pi is approximately %12.50f' % (22 /  7))
# the f in %12.50f is important ?!?!  code will not run without it 

# here is the new method
for i in range(1, 12):
	print('no. {0:2} squared is {1:4} and cubed is {2:4}'.format(i, i**2, i**3))
	
# if we wanted to do the same thing but left justify the texst we could insert <
for i in range(1, 12):
	print('no. {0:2} squared is {1:<4} and cubed is {2:<4}'.format(i, i**2, i**3))
	
# for percision 
print('Pi is approximately {0:12.50}'.format(22/7))

# we can use call our replacement fields out of order
print('January: {2}, February: {0}, March: {2}, April: {1}, May: {2}, June: {2}, July: {2}, August: {2}, September: {1}, October: {2}, November: {1}, December: {2}'.format(28, 30, 31))

#
for i in range(1, 12):
	print('no. {} squared is {} and cubed is {:4}'.format(i, i**2, i**3))
	
	
	
	
	




















