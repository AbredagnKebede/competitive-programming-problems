class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(speed):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + speed - 1) // speed
            return total_hours <= h

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canEatAll(mid):
                high = mid  
            else:
                low = mid + 1   
                

        return low
    