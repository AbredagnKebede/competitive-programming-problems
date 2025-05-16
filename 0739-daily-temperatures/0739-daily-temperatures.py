class SegmentTree:
    def __init__(self, size=101):   
        self.size = size
        self.tree = [float('inf')] * (4 * size)

    def update(self, pos, index, node=1, l=30, r=100):
        if l == r:
            self.tree[node] = index
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(pos, index, node * 2, l, mid)
        else:
            self.update(pos, index, node * 2 + 1, mid + 1, r)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, temp, node=1, l=30, r=100):
        if r < temp:
            return float('inf')
        if l >= temp:
            return self.tree[node]
        mid = (l + r) // 2
        return min(self.query(temp, node * 2, l, mid), self.query(temp, node * 2 + 1, mid + 1, r))

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        segment_tree = SegmentTree()

        for i in range(n - 1, -1, -1):
            warmer_index = segment_tree.query(temperatures[i] + 1)
            if warmer_index != float('inf'):
                answer[i] = warmer_index - i
            segment_tree.update(temperatures[i], i)

        return answer
 