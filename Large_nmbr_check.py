def largeNumber(num_1,num_2,num_3):
    if(num_1 >= num_2 and num_1 >= num_3):
        return num_1
    elif(num_2 >= num_1 and num_2 >= num_3):
        return num_2
    else:
        return num_3
    
num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
num3=int(input("Enter 3rd Number: "))

print("Large Number is: ", largeNumber(num1,num2,num3))
    
