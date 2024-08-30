# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = computeMid(nums)
        root = TreeNode(nums[mid])
        root.left = buildTree(nums[:mid])
        root.right = buildTree(nums[mid+1:])
        return root
        
        
        
        
def buildTree(arr):
    if arr == []:
        return None
    mid = computeMid(arr)
    node = TreeNode(arr[mid])
    node.left = buildTree(arr[:mid])
    node.right = buildTree(arr[mid+1:])
    return node
        
    
        
def computeMid(arr):
    start = 0
    end = len(arr) 
    mid = (start + end)//2
    return mid