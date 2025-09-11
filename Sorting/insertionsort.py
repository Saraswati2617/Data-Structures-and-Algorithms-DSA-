nums=[4,1,5,2,3]
n=len(nums)
for i in range(1,n):
    curr=nums[i]
    prev=i-1
    while prev>=0 and nums[prev]>curr:
        nums[prev+1]=nums[prev]
        prev-=1
    nums[prev+1]=curr

print(nums)
