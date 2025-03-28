class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            left, right = 0, 0 
            merged = []

            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] <= right_arr[right]:
                    merged.append(left_arr[left])
                    left += 1
                else:
                    merged.append(right_arr[right])
                    right += 1
            while left < len(left_arr):
                merged.append(left_arr[left])
                left += 1 
            while right < len(right_arr):
                merged.append(right_arr[right])
                right += 1
            
            return merged
        
        def mergesort(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            l_arr = mergesort(left, mid, arr)
            r_arr = mergesort(mid+1, right, arr)

            return merge(l_arr, r_arr)
        
        return mergesort(0, len(nums)-1, nums) 

