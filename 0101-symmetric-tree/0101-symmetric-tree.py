# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        left = []
        leftTree(root.left, left)
        right = []
        rightTree(root.right, right) 

        if len(left) != len(right):
            return False
        else:
            for i in range(len(left)):
                if left[i] != right[i]:
                    return False
        return True
        

def leftTree(node, tree):
    if node != None:
        tree.append(node.val)
        leftTree(node.left, tree)
        leftTree(node.right, tree)
    else:
        tree.append("null")

def rightTree(node, tree):
    if node != None:
        tree.append(node.val)
        rightTree(node.right, tree)
        rightTree(node.left, tree)
    else:
        tree.append("null")