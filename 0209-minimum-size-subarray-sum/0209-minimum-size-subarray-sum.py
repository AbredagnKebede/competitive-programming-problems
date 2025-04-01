class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res, curSum, l = len(nums)+1, 0, 0
        
        for r, n in enumerate(nums):
            curSum += n
            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1

        return res % (len(nums)+1)