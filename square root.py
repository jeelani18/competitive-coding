t=int(input())
l=0
h=t
while(l<=h):
    mid=(l+h)//2
    if(t<mid*mid):
        h=mid-1
    else:
        l=mid+1
print(h)
    
