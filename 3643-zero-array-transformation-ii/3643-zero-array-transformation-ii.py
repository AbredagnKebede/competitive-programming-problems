class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def helper(arr, q):
            res = [0]*(len(arr) + 1)
            for l, r, val in q:
                res[l] -= val
                res[r+1] += val

            cur = 0 
            temp = arr[:]
            for i in range(len(arr)):
                cur += res[i]
                temp[i] += cur 
                if temp[i] > 0: return False

            return True
        if all(num == 0 for num in nums):
            return 0
        best = -1
        min_k, max_k = 1, len(queries)
        while min_k <= max_k:
            mid = (min_k + max_k) // 2
            if helper(nums, queries[:mid]):
                best = mid
                max_k = mid - 1
            else:
                min_k = mid + 1
        
        return best