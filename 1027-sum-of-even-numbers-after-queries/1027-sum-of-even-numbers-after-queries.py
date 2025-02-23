class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        base_even_sum = sum(num for num in nums if num%2 == 0)

        for val, index in queries:

            prev = nums[index]
            cur = nums[index] + val
            nums[index] += val
            
            if prev%2 != 0 and cur%2 == 0:
                base_even_sum += cur
            elif prev%2 == 0 and cur%2 != 0:
                base_even_sum -= prev
            elif prev%2 == 0 and cur%2 == 0:
                base_even_sum += val

            answer.append(base_even_sum)             
        
        return answer
        