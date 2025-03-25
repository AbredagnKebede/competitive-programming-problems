class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(speed):
            total_hours = 0
            for i in piles:
                if i <= speed:
                    total_hours +=1
                elif i > speed:
                    if i%speed !=0: total_hours += (i//speed + 1)
                    else: total_hours +=(i//speed) 
            return total_hours <= h

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canEatAll(mid):
                high = mid  
            else:
                low = mid + 1   
                

        return low
    