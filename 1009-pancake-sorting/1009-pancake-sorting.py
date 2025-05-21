class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []
        ans = []
        for i in range(len(arr)-1, -1, -1):
            cur_max = max(arr[:i+1])
            max_index = arr.index(cur_max)

            if max_index == 0:
                arr[:i+1] = reversed(arr[:i+1]) 
                ans.append(i+1)
            else:
                arr[:max_index + 1] = reversed(arr[:max_index + 1]) 
                ans.append(max_index+1)
                arr[:i+1] = reversed(arr[:i+1]) 
                ans.append(i+1) 

        return ans
        