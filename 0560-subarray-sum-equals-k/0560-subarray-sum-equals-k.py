class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        cur_sum, cnt = 0, 0
        for i in nums:
            cur_sum += i

            if cur_sum - k in prefix:
                cnt += prefix[cur_sum - k]
            prefix[cur_sum] += 1
        return cnt
