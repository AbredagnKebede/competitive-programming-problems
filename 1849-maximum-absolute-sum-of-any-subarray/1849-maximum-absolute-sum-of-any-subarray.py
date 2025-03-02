class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        abs_max, abs_min, cur_max, cur_min = 0, 0, 0, 0

        for i in nums:
            cur_max = max(0, cur_max + i)   
            cur_min = min(0, cur_min + i)

            abs_max = max(abs_max, cur_max)
            abs_min = min(abs_min, cur_min)             
            
        return max(abs_max, abs(abs_min))
