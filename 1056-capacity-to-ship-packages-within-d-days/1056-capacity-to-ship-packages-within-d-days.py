class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        max_load = max(weights)
        daily = (len(weights) - 1) // days + 1  
        r = max_load * daily
        l = max(max_load, min(weights) * daily)

        def canship(cap):
            ship = 1
            currcap = cap

            for w in weights:
                if currcap - w < 0:
                    ship += 1
                    currcap = cap
                currcap -= w
            return ship <= days

        while l <= r:
            cap = (l + r) // 2
            if canship(cap):
                r = cap - 1
            else:
                l = cap + 1
        return l
