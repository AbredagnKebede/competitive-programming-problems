class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        cur_sum = cnt = 0

        for i in nums:
            cur_sum += i
            if cur_sum - goal in prefix:
                cnt += prefix[cur_sum - goal]
            prefix[cur_sum] += 1

        return cnt