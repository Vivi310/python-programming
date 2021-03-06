#!/usr/bin/env python3

## !NOTE! It's good to write shell bang for your script, remember how to write it!

## INSTRUCTIONS:
##
## Finish the following ninja practices
## To run this script make sure to add execute permission to the script, e.g.
##
##   $ chmod u+x <filename>.py
##
## Then run with this script with
##
##   $ ./<filename>.py
##

################################################################################
## 1 List1
## Take the following information as inputs:
##    fruits = ['Apple', 'Banana', 'Peach', 'Grape', 'Plum' ,'Lemon', 'Pear']
## Output the following lines:
##    1. Apple
##    2. Banana
##    3. Pear
##    4. Apple, Banana, Peach
##    5. Peach, Grape,Plum
##    6. Plum, Lemon, Pear

fruits = ['Apple', 'Banana', 'Peach', 'Grape', 'Plum', 'Lemon', 'Pear']
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[0:3])
print(fruits[2:5])
print(fruits[-3:])


################################################################################
## 2 List2
## Take the following information as inputs:
##    L = [
##        ['facebook, 'linkedin', 'amazon', 'google'],
##        ['Java','Python', 'Php'],
##        ['Bob','Tom','Jack']
##        ]
## Output the following lines:
##    1. facebook
##    2. Python
##    3. Jack


L = [
    ['facebook', 'linkedin', 'amazon', 'google'],
    ['Java','Python', 'Php'],
    ['Bob','Tom','Jack']
    ]
print(L[0][0])
print(L[1][1])
print(L[2][2])


################################################################################
## 3 Tuple1
## Take the following information as inputs:
##    classmates = ('Michael', 'Jack', 'Tom', 'Bob')
## Output the following lines:
##    1. Michael
##    2. Bob
##    3. Jack,Tom
##v   4. Tom,Bob

classmates = ('Michael', 'Jack', 'Tom', 'Bob')
print(classmates[0])
print(classmates[-1])
print(classmates[1:3])
print(classmates[-2:])


################################################################################
## 4 Tuple2
## Take the following information as inputs:
##    classmates = ('Michael', 'Jack', ['Tom', 'Bob'])
## Output the follwing lines:
##    1. Jack
##    2. Tom
##    3. Bob
##    4. Tom,Bob
## How to change 'Tom' to 'Jason', the classmates output:
##    classmates = ('Michael', 'Jack', ['Jason', 'Bob'])

classmates = ('Michael', 'Jack', ['Tom', 'Bob'])
print(classmates[1])
print(classmates[2][0])
print(classmates[2][1])
print(classmates[2])
classmates[2][0] = 'Jason'
print(classmates)


################################################################################
## 5 Find more built-in functions
## Python provide a bunch of built-in functions for your convenience, we've seen
## some of them:
##   int(), float(), str(), bool()  # convert variable type to int/float/string/bool
##   len()  # get length of a list or string
##   type()  # get type of a variable
##   input()  # get user input (stdin)
##   print()  # print object to standard output (stdout)
##   bin(), oct(), hex()  # convert a integer to binary/octal/hexical representation string
##   abs()  # get absolute value
##   max(), min()  # get max/min value of two object or a list
##   list(), tuple()  # convert to list/tuple
##
## Now we are going to meet more of them
##   all()  # return True if all elements of list are true
##   any()  # return True if any element of list is true
##   sum()  # sum up
##   sorted()  # reverse the list
##
## You can find the information at:
##   https://docs.python.org/3.5/library/functions.html
## Your task in the part, use the built-in function to find out the following information
##   1. Print result of all(), any() on list [True, False, True, True, False]
##   2. Print sum of list [12, 0, -5, -7, 11, 21, 55, -28]
##   3. Print sorted list of [12, 0, -5, -7, 11, 21, 55, -28]
##   4. Print max/min value of [12, 0, -5, -7, 11, 21, 55, -28]
##   5. Print length of list [12, 0, -5, -7, 11, 21, 55, -28]

list1 = [True, False, True, True, False]
print(all(list1))

list2 = [12, 0, -5, -7, 11, 21, 55, -28]
print(sum(list2))
print(sorted(list2))
print(max(list2))
print(min(list2))
print(len(list2))



l1 =[1,2,3,4,5,6,7,8,9,10]
print('sum = %d'%(sum(l1)))
s = 0
