# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.r_sum = 0
        def rev_inorder(node):
            if not node:
                return 
            rev_inorder(node.right)
            self.r_sum += node.val
            node.val = self.r_sum

            rev_inorder(node.left)

        rev_inorder(root)
        return root