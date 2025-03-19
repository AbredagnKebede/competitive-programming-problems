class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def back_track(start, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return 
            for i in range(start, n+1):
                cur.append(i)
                back_track(i+1, cur)
                cur.pop()

        back_track(1,[])
        return ans

            