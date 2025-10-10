class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_clos = float('inf')

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:                
                _3sum = nums[left] + nums[right] + nums[i]
                if abs(target - _3sum) < abs(target - best_clos):
                    best_clos = _3sum

                if _3sum > target:
                    right -= 1
                elif _3sum < target:
                    left += 1
                else:
                    return _3sum
        
        return best_clos
