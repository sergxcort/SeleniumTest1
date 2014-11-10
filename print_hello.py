__author__ = 'Sergey'
import math
import random

index = 0
array = []
array2 = []
array_max = []
max_value = []

#Matrix generating
for someint1 in range(3):
    array.append([random.randint(0,10), random.randint(0,10), random.randint(0,10)])

#Summ of elements in matrix
summ_last_two_items = array[0][-2:-1] + array[0][-1:]
summ_last_two_items = int(summ_last_two_items[0])+int(summ_last_two_items[1])

#Fucking min and max value
for someint2 in range(3):
    array2.append(array[someint2][1])

for someint1 in range(3):
    for someint2 in range(3):
        max_value.append(array[someint1][someint2])
        if array[someint1][someint2] == 4:
           know_value_what = someint1+1
min_value = min(array2)

#Max value
max_value = max(max_value)

print array, summ_last_two_items, min_value
print max_value, know_value_what

a = 10.0
b = 3.0
Result = math.modf(float(a)/float(b))

print Result[0]

























