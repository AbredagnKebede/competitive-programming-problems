class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        for i in range(len(nums)):
            j = i + 1
            result.append(nums[i])
            while j < len(nums):
                if j == len(nums):
                    result.append(sum(nums[i:]))
                else:
                    result.append(sum(nums[i:j+1])) 
                j +=1               
        result.sort()
        return sum(result[left-1:right])%1000000007
