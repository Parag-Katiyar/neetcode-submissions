# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        serial = []

        def arry(root): 

            #nonlocal serial

            if root is None: 
                serial.append("null")
                return

            serial.append(root.val)

            arry(root.left)
            arry(root.right)

            return
        
        arry(root)
        
        return ",".join(map(str, serial))


 
    # Decodes your encoded data to tree.

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        vals = data.split(",")
        self.index = 0  # Global pointer to track our position in the list
        
        def dfs():
            if vals[self.index] == "null":
                self.index += 1
                return None
            
            # Create the current root node
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            
            # Recursively build the left and right subtrees
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        return dfs()

























