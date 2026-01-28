class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        prefix, postfix = [nums[0]], [nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for j in range(len(nums)-2, -1, -1):
            postfix.append(nums[j]+postfix[-1])
        postfix.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                if postfix[i+1] == 0: return i
            elif i == len(nums)-1:
                if prefix[i-1] == 0: return i
            elif prefix[i-1] == postfix[i+1]:
                return i
        return -1

        