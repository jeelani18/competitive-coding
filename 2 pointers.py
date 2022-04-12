a=list(map(int,input().split()))
i=0
j=len(a)-1
if(len(a)%2)==0:
    while(i<len(a)//2):
        print(a[i],end=' ')
        print(a[j],end=' ')
        i+=1
        j-=1
else:
    while(i<len(a)//2):
        print(a[i],end=' ')
        print(a[j],end=' ')
        i+=1
        j-=1
    print(a[len(a)//2],0)
