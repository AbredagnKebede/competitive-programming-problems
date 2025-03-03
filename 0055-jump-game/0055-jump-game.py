class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        cur = 0
        for i in range(len(nums)):
            if i > cur:
                return False
                
            cur = max(cur, i + nums[i]) 
            if last - cur <= 0:
                return True
        return False