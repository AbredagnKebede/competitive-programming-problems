class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n == 0:
                return 1

            sub_pow = rec(x, n//2)
            return sub_pow*sub_pow if n%2 == 0 else sub_pow*sub_pow*x
        if n < 0:
            return 1/rec(x, -n)
        return rec(x, n)
 

        