# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(node):
            if not node:
                return [0, 0]
            
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)

            tot_sum = l_sum + r_sum + node.val
            tot_cnt = l_cnt + r_cnt + 1

            if tot_sum//tot_cnt == node.val:
                self.cnt += 1
                
            return [tot_sum, tot_cnt]
        dfs(root)
        return self.cnt

