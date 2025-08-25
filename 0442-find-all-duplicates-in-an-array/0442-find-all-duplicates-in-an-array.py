class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)        
        return [i for i in num_freq if num_freq[i] == 2]
 