# Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=nums.sort()
        # return n

        # zero=one=two=0
        # for i in nums:
        #     if i==0:
        #         zero+=1
        #     elif i==1:
        #         one+=1
        #     else:
        #         two+=1
        # for i in range(len(nums)):
        #     if zero>0:
        #         nums[i]=0
        #         zero-=1
        #     elif one>0:
        #         nums[i]=1
        #         one-=1
        #     else:
                
        #         nums[i]=2
        #         two-=1

        # return nums

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums