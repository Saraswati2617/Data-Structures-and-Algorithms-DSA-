# find the majority element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=len(nums)//2
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
            if dic[i]>s:
                return i