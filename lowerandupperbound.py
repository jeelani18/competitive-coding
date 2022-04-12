def lowerbound(arr,t):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)>>1
        if(arr[mid]>=t):
            right=mid-1
        else:
            left=mid+1
    return left
def upperbound(arr,t):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)>>1
        if(arr[mid]<=t):
            left=mid+1
        else:
            right=mid-1
    return right
arr=[2,2,5,6]
#0 1 2 3 4 5 6 6 8
t=7
l=lowerbound(nums,t)
x=upperbound(nums,t)
ans=[-1,-1]
if(l>x):
    return [-1,-1]
if(l>=0 and l<len(nums)and nums[l]==t):
    ans[0]=l
if(x<=len(nums)-1 and nums[x-1]==t):
    ans[1]=x   
if(x==l):
    return [l,l]
        #ans=[l,x]
print(ans)

