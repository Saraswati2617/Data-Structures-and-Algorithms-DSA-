nums=[4,1,5,2,3]
n=len(nums)
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)

