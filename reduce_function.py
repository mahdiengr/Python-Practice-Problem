from functools import reduce
initial_list = [1, 2, 3, 4, 5]
sum = reduce((lambda a,b: a+b),initial_list)
# sum
# for x in sum:
print (sum)