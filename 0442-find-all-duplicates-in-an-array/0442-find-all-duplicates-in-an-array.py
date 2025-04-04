class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            index = abs(num) - 1  
            
            if nums[index] < 0:  
                ans.append(abs(num))
            else:
                nums[index] *= -1  
        
        return ans
