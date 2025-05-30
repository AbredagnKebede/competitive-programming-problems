class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(binary):
            res = "".join('0' if i == '1' else '1' for i in binary)
            return res[::-1]
        
        stack = ['0']
        for i in range(2, n + 1):
            cur = stack[-1] + '1' + helper(stack[-1])
            stack.append(cur)
        
        return stack[-1][k-1]