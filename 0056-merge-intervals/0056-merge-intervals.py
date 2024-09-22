class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if intervals == []:
            return []
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            temp = intervals[i]
            prev = result[-1]
            if prev[0] <= temp[0] <= prev[1]:
                if temp[1] > prev[1]:
                    result[-1] = [prev[0], temp[1]]
                else:
                    result[-1] = [prev[0], prev[1]]
                
            else:
                result.append(temp)
                
        return result