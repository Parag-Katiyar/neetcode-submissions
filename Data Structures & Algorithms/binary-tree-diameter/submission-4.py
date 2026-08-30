# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0 


        def trav(root):

            nonlocal res

            if root is None: 
                return 0
                
            left_arm = trav(root.left)
            right_arm = trav(root.right)

            max_arm = max(left_arm, right_arm)

            diameter = left_arm + right_arm

            if diameter > res: 
                res = diameter

            return max_arm + 1

        trav(root)

        return res




