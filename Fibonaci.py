
def fibonaci(x,y):
    for i in range(100):
        z=x+y
        y=x
        x=z
        print(i, "= ",z)
fibonaci(0,1)
    # 1+0=1
    # 0+1=1
    # 1+1=2
    # 2+1=3