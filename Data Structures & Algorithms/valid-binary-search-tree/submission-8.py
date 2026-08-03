# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):
    def valid(node, min_val, max_val):
        # Base case: An empty node is always a valid BST
        if not node:
            return True
        
        # The current node's value must fall strictly within the bounds
        if not (min_val < node.val < max_val):
            return False
        
        # Recursively check the left and right subtrees with updated bounds
        return valid(node.left, min_val, node.val) and valid(node.right, node.val, max_val)

    # Initialize the bounds to negative and positive infinity
    return valid(root, float('-inf'), float('inf'))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return isValidBST(root)
        

        