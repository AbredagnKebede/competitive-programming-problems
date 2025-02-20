class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        prefix = [0]*(len(nums)+1)

        for start, end in requests:
            prefix[start] -= 1
            prefix[end+1] += 1

        prefix = sorted(list(itertools.accumulate(reversed(prefix))), reverse=True)
        
        return sum(count * value for count, value in zip(prefix, nums)) % (10**9 + 7)
