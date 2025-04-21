from functools import reduce
# num_1=4.34
# res = isinstance(num_1, float)  
# print(res)

numbers=[1,2.5,4.3,5.1,2,5,-2,0.01]

count_float=len(list(filter(lambda x: isinstance(x, float), numbers)))



print(count_float)