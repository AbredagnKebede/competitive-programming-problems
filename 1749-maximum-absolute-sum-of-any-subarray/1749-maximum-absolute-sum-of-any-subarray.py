from itertools import accumulate
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial=0))
        return max(prefix) - min(prefix)
        
