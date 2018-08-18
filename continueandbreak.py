#==================================================================
#						continue, break, else
#==================================================================

''' 
Date    : Fri 17 Aug 2018 05:01:24 PM PDT 
Subject : Program flow control
Title   : Lec 35 - continue, break, else
Source  : https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/t/lecture/3847262?start=0
''' 

#

'''
NOTES:

'''

# continue skips over a value
shopping_List1 = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shopping_List1:
	if item == 'spam':
		continue
# remember to have the same indentation for print() as for if()
	print('buy ' + item)

# break will end the statement
shopping_List2 = ['tune', 'chicken', 'bacon', 'bird', 'pork', 'ham']
for item in shopping_List2:
	if item == 'bird':
		break
	print('I should buy {}'.format(item))

# this other way 
meal = ['egg', 'bacon', 'spam', 'sausages']
for item in meal:
	if item == 'spam':
		nasty_food_item = item
		break
if nasty_food_item:
	print('cant i have anything without spam in it ')
	
# here is an example of a why we should declare this variable before the for loop
# if we do it this way without spam actually in the list, python errors;

'''
# i ran this program on its own and it errored 

  File "continueandbreak.py", line 53, in <module>
    if nasty_food_item:
NameError: name 'nasty_food_item' is not defined

# this because spam is never located so nasty var never gets created

meal = ['egg', 'bacon', 'tomato', 'sausages']
for item in meal:
	if item == 'spam':
		nasty_food_item = item
		break
if nasty_food_item:
	print('cant i ')
'''

# else can also be used in loops
meal = ['egg', 'bacon', 'pork', 'sausages']
nasty_food_item = ''
for item in meal:
	if item == 'spam':
		nasty_food_item = item
		break
else:
	print("i'll have a plate of that then , please")
	
if nasty_food_item == 'spam':
	print("can't i have anything without spam in it")
	
	
	
	


	
		
		
		
		














































































