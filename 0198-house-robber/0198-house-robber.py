class Solution:
    def rob(self, nums: List[int]) -> int:
        total1 = 0
        total2 = 0
        for i in nums:
            temp = max(i+total1, total2)
            total1 = total2
            total2 = temp
        
        return total2