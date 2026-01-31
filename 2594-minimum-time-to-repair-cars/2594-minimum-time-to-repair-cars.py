class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(time, rank):
            repaired = 0
            for i in range(len(rank)):
                can = int(sqrt(time/rank[i]))
                repaired += can

            return repaired >= cars
            
        best  = 0 
        min_time, max_time = 1, max(ranks)*cars**2
        while min_time <= max_time:
            mid = (min_time + max_time) // 2
            if helper(mid, ranks):
                best = mid
                max_time = mid - 1
            else:
                min_time = mid + 1
        
        return best
