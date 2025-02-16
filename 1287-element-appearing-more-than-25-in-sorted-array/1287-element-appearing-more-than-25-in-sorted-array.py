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

        # count_map = {}

        # for i in arr:
        #     if str(i) not in count_map:
        #         count_map[str(i)] = 1
        #     else:
        #         count_map[str(i)] += 1

        # sorted_count = dict(sorted(count_map.items(), key = lambda item: item[1], reverse = True))

        # return int(list(sorted_count.keys())[0])