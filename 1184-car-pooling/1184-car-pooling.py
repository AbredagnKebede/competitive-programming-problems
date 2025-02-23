class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        moves = []
        for numpass, start, end in trips:
            moves.append((start, numpass))
            moves.append((end, -numpass))
        have = 0
        moves.sort()
        for loc, num in moves:
            have += num
            if have > capacity:
                return False
                
        return True
