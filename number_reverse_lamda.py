number_strings = ['10', '2', '33', '5', '1']

numbers=[2,5,8,10,34,25]

numbers1=[1,2,4,5,2,5,-2]

num=sorted(number_strings , key=lambda x:int(x),reverse=True)
num1=sorted(numbers1, key=lambda x: x, reverse=True)
print(num)
print(num1)