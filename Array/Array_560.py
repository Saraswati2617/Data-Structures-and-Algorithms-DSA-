# Subarray sum equals k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countMap = defaultdict(int)
        countMap[0] = 1  # base case: a subarray starting from index 0
        currSum = 0
        result = 0
        
        for num in nums:
            currSum += num
            if currSum - k in countMap:
                result += countMap[currSum - k]
            countMap[currSum] += 1
        
        return result