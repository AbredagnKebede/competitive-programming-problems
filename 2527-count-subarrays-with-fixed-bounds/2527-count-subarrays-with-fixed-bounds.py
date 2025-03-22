class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min_index, last_max_index = -1, -1
        recent_invalid = -1

        cnt = 0
        for i in range(len(nums)):
            if nums[i] == minK:
                last_min_index = i
            if nums[i] == maxK:
                last_max_index = i
            
            if maxK < nums[i] or nums[i] < minK:
                recent_invalid = i
            #print(last_min_index, last_max_index, recent_invalid)
            if min(last_min_index, last_max_index) > recent_invalid:
                cnt += min(last_min_index, last_max_index) - recent_invalid

        return cnt
