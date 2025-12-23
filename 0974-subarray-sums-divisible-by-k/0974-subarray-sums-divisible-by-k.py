class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        cur_sum, cnt = 0, 0
        for i in nums:
            cur_sum += i
           
            if cur_sum%k in prefix_sum  :
                cnt += prefix_sum[cur_sum%k]
                        
            prefix_sum[cur_sum%k] += 1

        return  cnt