class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score, cur = 0, 0

        for p in s:
            if p == '(':
                stack.append(0)
            else:
                top = stack.pop()

                if top == 0:
                    cur = 1
                else:
                    cur = 2*top
                
                if not stack:
                    score += cur 
                else:
                    stack[-1] += cur
        return score