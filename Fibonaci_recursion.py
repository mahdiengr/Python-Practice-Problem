def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibo(n-1) + fibo(n-2))

  
#with serial number
# i=1
# print(i ,"= ",0)
# step=2
# while(i<12):
#     print(step,"= ",fibo(i))
#     i +=1
#     step +=1
i=1
print(0)
while(i<12):
    print(fibo(i))
    i +=1

