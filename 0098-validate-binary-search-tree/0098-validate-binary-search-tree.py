# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, l, r):
            if not node: return True 
            if not(node.val > l and node.val < r): return False
            return (helper(node.left, l, node.val) and helper(node.right, node.val, r))
        return helper(root, float('-inf'), float('inf'))