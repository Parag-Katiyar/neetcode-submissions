# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0 

        self.a = 0 

        def count(node,depth):

            if node == None: 
                return 
            self.a = max(self.a, depth)
            count(node.right, depth+1)
            count(node.left, depth+1)


        count(root,1)

        return self.a









        