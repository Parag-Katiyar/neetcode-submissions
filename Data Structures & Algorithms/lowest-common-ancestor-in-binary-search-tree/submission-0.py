# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#comparision and move in that direciton call the function again 
# if we encounter a node from where the tow values are in spereate nodes then we .. 
# if any node == any of the values then that node is the common lowest ancestor 

def low_an(node, val1, val2):

    if val1 == node.val: 

        return node

    if val2 == node.val: 

        return node

    if val1 > node.val and val2 > node.val: 

        return low_an(node.right, val1, val2)

    if val1 < node.val and val2 < node.val: 

        return low_an(node.left, val1, val2)

    if val1 < node.val or val2 > node.val: 

        return node

    if val1 > node.val or val2 < node.val: 

        return node

   


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        return low_an(root, p.val, q.val)


        
        


        


        
        