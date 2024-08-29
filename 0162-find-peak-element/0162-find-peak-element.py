class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            maxVal = max(nums)
            for j in range(len(nums)):
                if nums[j] == maxVal:
                    return j
        
        if len(nums) >= 3:
            for i in range(1, len(nums) - 1):
                first = nums[i-1]
                second = nums[i]
                third = nums[i+1]

                if second > first and second > third:
                    return i
            
            maxVal = max(nums)
            for j in range(len(nums)):
                if nums[j] == maxVal:
                    return j

        