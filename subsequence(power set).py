n=int(input('enter number of elements in a'))
a=list(map(int,input().split()))
for i in range(2**n):
    c=[]
    for j in range(n):
        if(i&(1<<j)):
            c.append(a[j])
    print(c)
