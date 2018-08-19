#==================================================================
#						Lecture 36 challange
#==================================================================

''' 
Date    : Sun 19 Aug 2018 03:43:51 PM PDT 
Subject : Augmented Assignment
Title   : augmented assignment in a loop
Source  : https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/quiz/4428958
''' 

#

'''
NOTES:

Early computers couls only perform addition.  In order to multiply one number by another, they performed
repeated addition.

For example 5*8 was performed by adding 5 eight times

5+5+5+5+5+5+5+5 = 40

Use a for loop and augmented assignment, to give answer the result of multiplying number by multiplier

Paste your code into your IDE, and make sure it works with different values for number and multilier.
Note that this exercise checking system will only validate your code with the values 5 and 8, for number
and multiplier

'''

# Lec 36 challange 
number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
	answer += number
print(answer)
	
	
	
















































































