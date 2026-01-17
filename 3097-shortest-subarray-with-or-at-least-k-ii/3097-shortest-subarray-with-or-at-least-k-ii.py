class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        hash_set = {} 
        size = inf

        for r, num in enumerate(nums):
            hash_set = {val | num: l for val, l in hash_set.items()}
            hash_set[num] = r
            
            for val, l in hash_set.items():
                if val >= k:
                    size = min(size, r - l + 1)
        
        if size == inf:
            return -1
        return size
