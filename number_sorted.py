number_strings = ['10', '2', '33', '5', '1']

num=sorted(number_strings , key=lambda x:int(x),reverse=True)
print(num)