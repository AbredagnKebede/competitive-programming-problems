class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(val, arr):
            get = 0
            for i in range(len(arr)):
                if arr[i] >= val:
                    get += arr[i] // val

            return get >= k
        
        best = 0 
        min_candy, max_candy = 1, max(candies)
        while min_candy <= max_candy:
            mid = (min_candy + max_candy) // 2
            if helper(mid, candies):
                best = mid
                min_candy = mid + 1
            else:
                max_candy = mid - 1

        return best