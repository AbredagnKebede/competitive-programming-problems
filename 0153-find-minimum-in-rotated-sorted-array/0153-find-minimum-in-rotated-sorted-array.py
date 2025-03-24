class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]: return nums[0]
        l, r = 0, 1
        while nums[l] < nums[r]:
            l +=1
            r +=1
        return nums[r]