class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, cnt, window = 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
           
            window = max(window, right - left + 1)
                 
        return window
