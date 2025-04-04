class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(instructions)
        bit = BIT(max_num)
        cost = 0
        
        for i, num in enumerate(instructions):
            left = bit.query(num - 1)               
            right = i - bit.query(num) 
            cost += min(left, right)
            bit.update(num, 1)
        
        return cost % MOD
