# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result, Tree = [] , [root]
        while Tree:
            node = Tree.pop()
            result.append(node.val)
            if node.left:
                Tree.append(node.left)
            if node.right:
                Tree.append(node.right)
        return result[::-1]