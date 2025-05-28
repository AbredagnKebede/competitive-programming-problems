class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distance = [0]*n
        distance[start_node] = 1
        for i in range(n-1):
            flag = False
            for j, (k, l) in enumerate(edges):
                if distance[k] * succProb[j] > distance[l]:
                    distance[l] = distance[k] * succProb[j]
                    flag = True
                if distance[l] * succProb[j] > distance[k]:
                    distance[k] = distance[l] * succProb[j]
                    falg = True
            if not flag:
                break
        
        return distance[end_node]