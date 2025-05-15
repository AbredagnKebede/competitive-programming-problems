class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        ops, prime = 0, 2        
        while n > 1:
            while n % prime == 0:
                ops += prime
                n //= prime
            prime += 1
            
        return ops