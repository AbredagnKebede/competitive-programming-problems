class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        second_max = float('-inf')  

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] < second_max:
                return True
            
            while stack and stack[-1] < nums[j]:
                second_max = stack.pop()
            
            stack.append(nums[j])
        
        return False
