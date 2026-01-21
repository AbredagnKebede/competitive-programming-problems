class Solution:
    def maximumSubarraySum(self, nums, k):
        s = sum(nums[:k])
        d = {n: i for i, n in enumerate(nums[:k])}
        ms = s if len(d) == k else 0
        for i in range(k, len(nums)):
            s += nums[i] - nums[i-k]
            d[nums[i]] = i
            if d[nums[i-k]] == i-k:
                del d[nums[i-k]]
            if len(d) == k:
                ms = max(s, ms)

        return ms