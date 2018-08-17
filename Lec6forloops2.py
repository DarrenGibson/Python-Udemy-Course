#=================================================================#
#			 Pyhton Section 6 Lecture 34 for loops con't
#-----------------------------------------------------------------#

'''
Date		: Fri 17 Aug 2018 02:59:33 PM PDT  
Author		: Darren Gibson
Title		: Section 6: Lec 34 - for loops con't
Resources	: https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3840226?start=0\
'''

# Lec 34 - for loops con't

'''
NOTES:
range is a sequence type,     we put data in?!?!?

'''

# 

number = '9,223,372,036,854,775,807'
cleanedNumber = ''

for char in number:
	if char in '0123456789':
		cleanedNumber = cleanedNumber + char
		
newNumber = int(cleanedNumber)
print('the number is {}'.format(newNumber))

# we can index trough lists like this
for j in ['not pinin', 'no more', 'a stiff', 'breath of life']:
# two good output options
	print('this parrot is ' + j)
	print('this parrot is {} '.format(j))

# there is another argument/parameter?! available in our for loop
# that lets us step trough our values?indexes?parameters?
for i in range(0, 100, 5):
	print('i is {} '.format(i))

for i in range(1, 13):
	for j in range(1, 13):
# i have included some spacing after {} but it doesn't completely resovle the issue
		print('{}   times {}   is {}'.format(i, j, i*j))
# notice when we place this print function back with the first for command it
# only apppears every 12th line
	print('=========================')

# Lecture 34, extract capitals challange








































