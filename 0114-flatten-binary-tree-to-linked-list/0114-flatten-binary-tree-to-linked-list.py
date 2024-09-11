# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp1 = []
        temp2 = []
        if root == None:
            return None
        
        head = root
        
        readTree(root.left,temp1)
        readTree(root.right,temp2)
        
        final = temp1 + temp2
        if len(final) == 0:
            return root
        
        i = 0
        while i < len(final):
            head.left = None
            head.right = TreeNode(final[i])
            head = head.right
            i += 1
        return root
        
        
        
def readTree(node, tree):
    if node != None:
        tree.append(node.val)
        readTree(node.left, tree)
        readTree(node.right, tree)