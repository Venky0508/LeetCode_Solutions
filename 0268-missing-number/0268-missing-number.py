class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = sorted(nums,reverse = True)
        print(arr)    
        for i in range(len(arr)):
            val = len(arr) - i
            if arr[i] != val:
                return val
        return 0