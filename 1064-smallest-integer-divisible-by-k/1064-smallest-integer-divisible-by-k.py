class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        modulo = 0
        for n in range(1,K+1):
            num = modulo*10+1
            modulo = (num) % K
            if modulo == 0:
                return n

        return -1