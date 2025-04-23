class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        return [i for i in count_nums if count_nums[i] > len(nums)/3]