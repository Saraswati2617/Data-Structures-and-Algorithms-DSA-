# Max consecutive ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        new_max=0
        for i in range(len(nums)):
            if nums[i]==1:
                m+=1
                new_max=max(new_max,m)
            if nums[i]==0:
                # new_max=max(new_max,m)
                m=0
        return new_max

            