class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_ramp = 0
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                max_ramp = max(max_ramp, i - stack[-1])
                stack.pop()
        
        return max_ramp