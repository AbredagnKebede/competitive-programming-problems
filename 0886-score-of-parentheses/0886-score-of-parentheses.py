class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, cur = 0, 0

        for i, p in enumerate(s):
            if p == '(':
                cur += 1
            else:
                cur -= 1
                if s[i-1] == '(':
                    score += 2**cur 

        return score