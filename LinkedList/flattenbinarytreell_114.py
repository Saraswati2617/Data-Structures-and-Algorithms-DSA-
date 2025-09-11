class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                # Connect it to current's right
                prev.right = curr.right
                # Move left subtree to right
                curr.right = curr.left
                curr.left = None
            # Move to next node
            curr = curr.right