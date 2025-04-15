
def fibonaci(x,y):
    i=1
    print(i,"= ", 0)
    
    i=2
    if(x==0):
        while(i<=12):
            z=x+y
            y=x
            x=z
            print(i, "= ",z)
            i +=1
    elif(y==0):
        while(i<=12):
            z=x+y
            x=y
            y=z
            print(i, "= ",z)
            i +=1
        
fibonaci(0,1)
    # 1+0=1
    # 0+1=1
    # 1+1=2
    # 2+1=3
