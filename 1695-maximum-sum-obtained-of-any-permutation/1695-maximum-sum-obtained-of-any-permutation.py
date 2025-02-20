class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        prefix = [0]*(len(nums)+1)
        for start, end in requests:
            prefix[start] += -1
            prefix[end + 1] += 1

        hashmap = defaultdict(int)
        add = 0
        for i in reversed(range(1, len(prefix))):
            add += prefix[i]
            hashmap[i-1] += add 

        hashmap = dict(sorted(hashmap.items(), key = lambda item: item[1], reverse=True))
        ans = [0]*len(nums)
        cur = 0
        for i in hashmap:
            ans[i] = nums[cur]
            cur += 1
        for _ in range(1, len(ans)):
            ans[_] += ans[_-1]

        max_sum = 0
        for start, end in requests:
            max_sum += (ans[end] - ans[start - 1]) if start != 0 else ans[end]

        return max_sum % (10**9 + 7)
        