# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
        if not root:
            return -1
        
        elements.append(root.val)
        readTree(root.left, elements)
        readTree(root.right, elements)
        
        elements.sort()
        return elements[k-1]
    
def readTree(node, tree):
    if node != None:
        tree.append(node.val)
        readTree(node.left, tree)
        readTree(node.right, tree)
        