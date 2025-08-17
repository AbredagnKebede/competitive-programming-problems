# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(node, level):
            if not node:
                return 
            
            if len(result) == level:
                result.append(deque())
            if level%2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return [list(i) for i in result]