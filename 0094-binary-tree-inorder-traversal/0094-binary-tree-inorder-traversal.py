# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        final = []
        readTree(root, final)
        
        return final
    
    
def readTree(node, tree):
    if node != None:
        readTree(node.left, tree)
        tree.append(node.val)
        readTree(node.right, tree)
        