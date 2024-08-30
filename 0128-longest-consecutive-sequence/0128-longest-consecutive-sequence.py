class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # maxElement = max(nums)
        # minElement = min(nums)
        # buffer = 0
        # if minELement > 0:
        #     countArr = [0] * (maxElement + 1)
        # else:
        #     buffer = minElement * (-1)
        #     countArr = [0] * ((maxElement + 1) + buffer)
        
        uniques = set(nums)
        max_length = 0

        while len(uniques) != 0:
            low = uniques.pop()
            high = low
            
            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1
                
                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length
            
        