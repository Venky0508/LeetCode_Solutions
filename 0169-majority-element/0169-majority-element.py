class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        
        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else:
                countMap[i] += 1
        
        for key, value in countMap.items():
            if value > (len(nums)//2):
                return key