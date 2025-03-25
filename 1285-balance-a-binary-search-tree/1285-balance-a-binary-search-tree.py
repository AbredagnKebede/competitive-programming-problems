# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def in_order(node, nodes_array):
            if not node:
                return 
            in_order(node.left, nodes_array)
            nodes_array.append(node)
            in_order(node.right, nodes_array)

        def sort_to_BST(arr, left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            new_node = arr[mid] 

            new_node.left = sort_to_BST(arr, left, mid - 1)
            new_node.right = sort_to_BST(arr, mid + 1, right)

            return new_node 

        nodes_array = []
        in_order(root, nodes_array)
        
        return sort_to_BST(nodes_array, 0, len(nodes_array) - 1)

