# Missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(range(1, len(nums)+1))
        s=sum(nums)
        return total-s