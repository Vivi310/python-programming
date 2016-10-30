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
## 1 Loop exercise 1
## Please print each element in list:
##    value_list = [1,2,3,4,5,6,7,8]
## Output the following format:
##    1. output the length of value_list:
##        length = 8
##    2. output each element:
##        1,2,3,4,5,6,7,8
##    3. output each even element:
##        2,4,6,8
##    4. output each odd element:
##        1,3,5,7
##    5. output each reversed element
##        8,7,6,5,4,3,2,1
##    6. output the sum of all elements:
##        sum = 36
##    7. output the max element of value_list
##        max_value = 8
##    8. output the min element of value_list
##        min_value = 1

vl = [1,2,3,4,5,6,7,8]
print('length = %d'%(len(vl)))

print(vl)

for n in vl:
    if n%2 == 0:
        print(n)

for m in vl:
    if m%2 ==1:
        print(m)

#print('reversed = %d'%(reversed(vl)))


print('sum = %d'%(sum(vl)))

print('max = %d'%(max(vl)))

print('min = %d'%(min(vl)))


#################################################################################
## 2 List comprehension exercise 2
##    data = "123,,456,789,,,,34,,,,12"
##Output the following format:
##    1. result = [123,456,789,34,12]

data = "123,,456,789,,,,34,,,,12"
data = int(data)
print('data = ', split',')








#################################################################################
## 3 exercise 3
##    data = [1,3,2,5,4,8,6,7]
##Output the following format
##    1. append a element '9'(use append() function)
##       data = [1,3,2,5,4,8,6,7,9]
##    2. insert a element '10' at index 2(use insert() function)
##       data = [1,3,10,2,5,4,8,6,7,9]
##    3. return final element and delete from list(use pop() function)
##       data = [1,3,10,2,5,4,8,6,7]
##    4. sort elements in list(use sort() function)
##       data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
##    5. reverse elements in list(use reverse() function)
##       data = [10, 8, 7, 6, 5, 4, 3, 2, 1]


data = [1,3,2,5,4,8,6,7]
data.append(9)


data.insert(2, 10)
print(data)

data.pop()
print(data)

data.sort()
print(data)

data.reverse()
print(data)


##################################################################################
## 4 exercise 4
## use 'while' statement to calculate the sum from 1 to 100
## input:
##    n = 100
##    sum = 0
##    counter = 1
##    while(){...finished by yourself...}
##    print(sum)
## output:
##    sum = 5050

n = 100
sum = 0
counter = 1
while n > 0:
    sum = sum + n
    n =n - 1
print(sum)





##################################################################################
## 5 exercise 5
## Please judge the year that you input is leap year
## for example:
##    2000, 1922,2400 is leap year
##    2011, 2013 is not leap year
##
## input:
##    year = int(raw_input('Please enter the year'))
##    ... finished by yourself...
##
## output:
##    for example : 2000 is leap year.
##                  2011 is not leap year

year = int(input('please enter the year: '))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('%04d is leap year.'%(year))
        else:
            print('%04d is not leap year.'%(year))
    else:
        print('%04d is leap year.'%(year))
else:
    print('%04d is not leap year.'%(year))




###################################################################################
## 6 exercise 6
## Please find prime number from list
## input:
##    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
## output:
##    result = [2,3,5,7,11,13,17,19]

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for x in data:
    if x%2 == 0 and x>=2:
        if x%3 == 0 and x>=3:
            if x%5 == 0 and x>=5:
                if x%7 == 0 and x>=7:
                    print(x)



