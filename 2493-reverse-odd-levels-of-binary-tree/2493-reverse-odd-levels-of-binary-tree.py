# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(leftnode, rightnode, level):
            if not leftnode or not rightnode:
                return 
            if level%2 == 0:
                leftnode.val, rightnode.val = rightnode.val, leftnode.val

            dfs(leftnode.left, rightnode.right, level + 1)
            dfs(leftnode.right, rightnode.left, level + 1)

        dfs(root.left, root.right, 0)
        return root