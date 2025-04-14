from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = Counter(nums)
        numMap = sorted(numMap.items(), key=lambda x:x[1], reverse=True)
        result = []
        for j in numMap[:k]:
            result.append(j[0])

        return result

        