# Move zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                while nums[j]==0 and j<len(nums)-1:
                    j+=1
                nums[i]=nums[j]
                nums[j]=0
        return nums
                
        # l = 0
        # for r in range(0, len(nums)):
        #     # print(f" l: {l} r: {r}-- {nums}")
        #     if nums[r] !=0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l = l + 1
        # # print(f" l: {l} r: {r}-- {nums}")
        # return nums

        