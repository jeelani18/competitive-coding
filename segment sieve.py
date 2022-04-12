L,R=map(int,input().split())
n=1000001
def sieve(n):
    c[1]*n
    c[0]=0
    c[1]=0
    for i in range(2,n+1):
        if(c[i]==1):
            for j in range(i*i,n+1,i):
                c[i]=0
def primes(R):
    d=[]
    for i in range(2,R+1):
        if(c[i]==1):
            d.append(c[i])
for i in d:
    a=[]
    f=(L//i)*i
    if(f<L):
        f+=i
    for j in range(max(f,i*i),R+1,i):
        a[j-L]=0
for 
    

        
    
            
            
