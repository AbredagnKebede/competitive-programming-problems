class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right):
            if left == right:
                return nums[right]
            
            left_score = nums[left] - play(left + 1, right)
            right_score = nums[right] - play(left, right - 1)
            return max(left_score, right_score)
        
        return play(0, len(nums) - 1) >= 0 