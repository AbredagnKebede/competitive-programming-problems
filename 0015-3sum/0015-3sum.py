class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                II_sum = nums[left] + nums[right]
                if II_sum == target:
                    result.add((nums[i], nums[left], nums[right])) 
                    left +=1
                    right -=1
                elif II_sum < target:
                    left +=1
                else:
                    right -=1
        return  result
                                       