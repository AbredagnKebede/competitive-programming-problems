class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canBePutIn(distance, x, n):
            prev = x[0]
            n -= 1
            for i in range(1, len(x)):
                if x[i] - prev >= distance:
                    n -= 1
                    prev = x[i]
            return n <= 0         
        position.sort()
        min_s, max_s = 1, max(position) - min(position)
        best = 0
        while min_s <= max_s:
            mid = (min_s + max_s) // 2
            if canBePutIn(mid, position, m):
                best = mid
                min_s = mid + 1
            else:
                max_s = mid - 1
        
        return best