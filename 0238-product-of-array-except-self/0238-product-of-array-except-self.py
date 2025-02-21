class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        cur_product = 1
        for i in range(len(nums)):
            prefix[i] = cur_product
            cur_product *= nums[i]
        post_product = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= post_product
            post_product *= nums[i]
        
        return prefix


        