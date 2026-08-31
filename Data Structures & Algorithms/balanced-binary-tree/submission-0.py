# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balance(root): 

            if root is None: 
                return 0

            left_arm = balance(root.left)
            right_arm = balance(root.right)

            if left_arm is False or right_arm is False: 
                return False

            elif abs(left_arm - right_arm) > 1: 
                return False

            else:
                return max(left_arm,right_arm) + 1

        x = balance(root)

        if x is False: 
            return False
        else: 
            return True 

        
        















