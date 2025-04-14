class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        print(len(intervals))
        intervals.sort(key=lambda x:x[0])
        result = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if next_start <= end and next_start >= start:
                end = next_end
            else:
                result.append([start,end])
                start = next_start
                end = next_end
                
            if i == len(intervals) - 1:
                result.append([start,end])

        return result
