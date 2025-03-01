class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:

            width = right - left
            min_height = min(height[left], height[right])
            max_water = max(max_water, width * min_height)

            if height[left] < height[right]:
                prev = height[left]
                while left < right and height[left] <= prev:
                    left += 1
            else:
                prev = height[right]
                while left < right and height[right] <= prev:
                    right -= 1

        return max_water
 