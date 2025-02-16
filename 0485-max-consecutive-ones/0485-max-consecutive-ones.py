class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        prev = -1
  

        for i in nums:
            if prev == i and  i == 1:
                count += 1
            elif i == 1:
                prev = i
                count = 1
            else:
                prev = i 
                continue

            if count > maxCount:
                maxCount = count

        return maxCount