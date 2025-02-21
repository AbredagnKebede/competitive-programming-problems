class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sumNow = 0
        for i in nums:
            if sumNow < 0:
                sumNow = 0
            sumNow += i
            maxSum = max(maxSum, sumNow)
        return maxSum

