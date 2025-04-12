class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        result = 0
        for i in range(0,len(arr),2):
            pair = min(arr[i],arr[i+1])
            result += pair

        return result



