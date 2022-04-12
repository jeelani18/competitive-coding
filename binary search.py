a=list(map(int,input().split()))
l=0
h=len(a)-1
m=len(a)//2
t=int(input())
while(l<h):
    if(t==a[m]):
        print('t is found')
        break
    elif(a[m]<t):
        l=m+1
        m=(l+h)>>1
    elif(a[m]>t):
        h=m-1
        m=(l+h)>>1
else:
    print('not found')
