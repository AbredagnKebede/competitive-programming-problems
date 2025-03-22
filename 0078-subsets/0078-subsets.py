class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(start, cur):
            result.append(cur[:])
                
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return result
