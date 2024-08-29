class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        ans = set()
        for val in count.values():
            if val not in ans:
                ans.add(val)
            else:
                return False
        
        return True
        