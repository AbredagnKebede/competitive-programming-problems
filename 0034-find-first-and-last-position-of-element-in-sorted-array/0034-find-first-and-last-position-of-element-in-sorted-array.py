class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans[0] = mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans[1] = mid
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans