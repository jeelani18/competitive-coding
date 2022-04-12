n=int(input())
a=[1,3,5,6]


for i in range(len(a)):#0
    for j in range(i+1,len(a)+1):#1
        print(a[i:j])#0 to 1
