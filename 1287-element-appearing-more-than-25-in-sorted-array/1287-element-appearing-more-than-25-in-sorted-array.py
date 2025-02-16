import math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        
        prev = arr[0] 
        count = 1
        max_count = 0
        ans = 0
        for i in range(1, len(arr)):
            if count > max_count:
                max_count = count
                ans = prev
            
            curr = arr[i]
            if curr == prev:
                count += 1
            else:
                prev = curr
                count = 1

        if count > max_count:
                max_count = count
                ans = prev

        return ans