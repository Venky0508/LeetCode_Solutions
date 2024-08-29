import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # answer = []
        # temp = []
        # for p in potions:
        #     val = math.ceil(success/p)
        #     temp.append(val)
        # temp.sort()
        # total = len(temp)
        # for s in spells:
        #     count = 0
        #     for i in range(len(temp)):
        #         if temp[i] <= s:
        #             count += 1
        #         elif temp[i] > s:
        #             break
        #     answer.append(count)
        # return answer

        answer = []
        potions.sort()

        for s in spells:
            potion_needed = (success + s - 1) // s
            left = 0
            right = len(potions)
            while left < right:
                mid = left + (right - left) // 2
                if potions[mid] >= potion_needed:
                    right = mid
                else:
                    left = mid + 1
            count = len(potions) - left
            answer.append(count)

        return answer


        





