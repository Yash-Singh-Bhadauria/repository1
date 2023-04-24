n=int(input('Give the no. of terms to be found:')
x=0
y=1
i=1
while i<=n:
    print(x)
    x,y=y,y+x
    i+=1
