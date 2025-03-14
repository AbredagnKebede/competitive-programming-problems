class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def getMin(node):
            while node.left:
                node = node.left
            return node
        
        if not root:
            return None
        
        if root.val > val:
            root.left = self.deleteNode(root.left, val)
        elif root.val < val:
            root.right = self.deleteNode(root.right, val)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                new = getMin(root.right)
                root.val = new.val
                root.right = self.deleteNode(root.right, new.val)
            
        return root
            