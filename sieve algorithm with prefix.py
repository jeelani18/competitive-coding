def sieve_prefix(n):
    sieve=[]
    count=0
    prefix=[]
    for i in range(n+1):
        sieve.append(True)
    sieve[0]=False
    sieve[1]=False
    for i in range(len(sieve)):
        prefix.append(0)
    for i in range(2,n+1):
        if(sieve[i]==True):
            for j in range(i*i,n+1,i):
                sieve[j]=False
    prefix[0]=sieve[0]
    for i in range(1,len(prefix)):
        prefix[i]=prefix[i-1]+sieve[i]
    return prefix[n]
t=int(input())
for i in range(t):
    n=int(input())
    print(sieve_prefix(n))
    

    

    
        
