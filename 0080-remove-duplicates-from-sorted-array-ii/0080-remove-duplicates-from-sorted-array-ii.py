class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countMap = {}
        
        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else:
                val = countMap[i]
                if val < 2:
                    countMap[i] += 1
        
        pointer = 0
        for key, val in countMap.items():
            if val == 1:
                nums[pointer] = key
                pointer += 1
            else:
                nums[pointer] = key
                pointer += 1
                nums[pointer] = key
                pointer += 1
        
        return pointer
                    