class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        balance = 0
        found = False
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0

        for num in nums:
            if num < k:
                balance -= 1
            elif num > k:
                balance += 1
            else:
                found = True   
            
            if found:
                result += prefix_count[balance] + prefix_count[balance - 1]
            else:
                prefix_count[balance] += 1

        return result
