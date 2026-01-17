from collections import defaultdict

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        maxb = defaultdict(int)
        minb1 = 0
        items.sort(key = lambda x:x[0])
        pp = None
        maxb[items[0][0]] = items[0][1]
        for i1 in range(1,len(items)):
            i = items[i1]
            maxb[i[0]] = max(maxb[items[i1-1][0]], i[1])
        
        k = list(maxb.keys())
        
        ans = []
        for q in queries:
            if maxb[q]==0:
                qq = bisect_right(k,q)
                if qq>0:
                    maxb[q]=maxb[k[qq-1]]
                else:
                    maxb[q]=0
            ans.append(maxb[q])
        return ans