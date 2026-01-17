class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True     
        def generate_nPrimes(n):
            if n < 2:
                return    

            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False   

            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:            
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            primes = [i for i, prime in enumerate(is_prime) if prime]
            primes.insert(0,0)
            return primes

        n, prev = max(nums), float('-inf')
        prime_array = generate_nPrimes(n)
    
        for i in range(len(nums)):
            current_num = nums[i]
            r, l = bisect.bisect_left(prime_array, current_num) - 1, 0
            if current_num - prime_array[l] <= prev:
                return False
            while r >=l:
                minPrimesub = current_num - prime_array[r]
                if minPrimesub > prev:
                    nums[i] = minPrimesub
                    prev = minPrimesub
                    break
                r -=1
        return len(set(nums)) == len(nums) and nums == sorted(nums)
        

