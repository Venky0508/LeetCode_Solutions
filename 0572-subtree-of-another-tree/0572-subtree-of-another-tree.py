# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        tree = []
        subTree = []

        readTree(root,tree)
        readTree(subRoot,subTree)
        temp2 = ''.join(subTree)
        if len(tree) == len(subTree):
            temp1 = ''.join(tree)
            if temp1 == temp2:
                return True

        for i in range(len(tree)-len(subTree) + 1):
            sub = tree[i:i+len(subTree)]
            temp1 = ''.join(sub)
            if temp1 == temp2:
                return True

        return False


def readTree(node, tree):
    if node != None:
        tree.append(str(node.val))
        readTree(node.left, tree)
        readTree(node.right, tree)
    else:
        tree.append("null")
        