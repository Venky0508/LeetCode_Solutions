class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums) - 1, -1)

def binary_search(arr, target, left, right, prev):
    mid = (right - left)//2 + left

    if arr[mid] == target:
        return mid
    
    if mid == prev:
        return prev + 1
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid-1, mid)
    else:
        return binary_search(arr, target, mid+1, right, mid)