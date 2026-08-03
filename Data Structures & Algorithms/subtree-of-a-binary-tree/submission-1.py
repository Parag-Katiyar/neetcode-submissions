# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find(node, root, realroot):

    if root == None and node == None: 
        return True      

    if node == None and root != None: 
        return False  

    if node!= None and root ==None:
        return False
    

    if root == realroot:

        if node.val != root.val:
            if find(node.right, root, realroot) or find(node.left, root, realroot):
                return True

        
        elif node.val == root.val:
            if find(node.right, root.right, realroot) and find(node.left, root.left, realroot):
                return True 
            if find(node.right, root, realroot) or find(node.left, root, realroot):
                return True
            
    if root != realroot: 

        if node.val == root.val:
            if find(node.right, root.right, realroot) and find(node.left, root.left, realroot):
                return True 
            return False
            
        elif node.val!=root.val: 
            return False 

    
    return False 



class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return find(root, subRoot, subRoot)

        















        
        