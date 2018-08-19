#==================================================================
#						Augmented Assingment
#==================================================================

''' 
Date    : Fri 17 Aug 2018 10:38:00 PM PDT 
Subject : Section 6
Title   : Lecture 36 - Augmented assignment
Source  : https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3855720?start=0
''' 

#

'''
NOTES:

'''

# 
number = '9,223,372,036,854,775,807'
cleanedNumber = ''
for i in range(0, len(number)):
	if number[i] in '0123456789':
# cleanedNumber = cleanedNumber + number[i]    we can augment this statement with  
		cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print('The number is {}'.format(newNumber))

# some augmented assignment examples
x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)
# we get 25.0 because this is a floating point number
x **= 2
print(x)
# same here 152625.0
x %= 60
print(x)
# here as well 25.0

# there are 2 different binary operators we can use on strings Concatenation and repition
greeting = 'good '
greeting += 'morning'
print(greeting)

# i tried this without the = and it only printed it once?
greeting *= 5
print(greeting)

# these are the only binary operators that we can use with strings
# there are 5 binary operators
# += -= *= /= %= **' <<= >>= &= ^= |=


















































































