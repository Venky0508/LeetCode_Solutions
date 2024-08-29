# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        return delNode(root, key)

def delNode(node, key):
    if node == None:
        return None
    if node.val > key:
        node.left = delNode(node.left, key)
    elif node.val < key:
        node.right = delNode(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            n = node.right
            while n .left:
                n = n.left
            node.val = n.val
            node.right = delNode(node.right, n.val)

    return node
        
