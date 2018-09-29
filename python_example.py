### This is a sample file

import math

### Variables Example
a = 3
b = 5
c = a + b
print(c)

### Variable types
d = 1
e = 'Sam'
f = False
g = 1.1
print("The variable types are:\nd is {}\ne is {}\nf is {}\n g is {}\n".format(type(d),type(e),type(f),type(g)))

### Loops

### For Loops
for x in range(1,10): #x takes on the value of each value in the range
	print(x)

### While loops
state = True
i = 0
while state: # as long as State is TRUE, the loop runs
	print(i)
	i = i + 1
	if i == 80:
		state = False #by setting state to False we break the loop

### Data structures
_list1 = ['dog','runs','very','fast']
_list2 = [14,5,2,3,4,5]

### print list1
sentence = "" #create a senetence variable
for x in _list1:
	sentence = sentence + " " + x #add all elements of list1 into a single sentence
print(sentence)

### add all elements of _list2
j = 0
for x in _list2:
	j = j + x #or j += x
print("The sum of _list2 is {}".format(j))

_dictionary = {	'Sam' 	 : 'male',
				'Hannah' : 'female'}

### accessing a dictionary
print(_dictionary['Sam']) #returns male
print(_dictionary['Hannah']) #returns female

