# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = {}
        
        if not root:
            return []
        
        level = 0
        tree[level] = [root.val]
        readTree(root.left, tree, level+1)
        readTree(root.right, tree, level+1)
        return  tree.values()
    
        

        
def readTree(node, tree, level):
    if node:
        if level not in tree:
            tree[level] =[node.val]
        else:
            tree[level].append(node.val)
        readTree(node.left, tree, level+1)
        readTree(node.right, tree, level+1)