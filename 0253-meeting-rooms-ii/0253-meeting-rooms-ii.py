class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals = [[7,10],[2,4]]
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        used_room = []
        heapq.heapify(used_room)
        used_room.append(intervals[0][1]) #heap
        for row in intervals[1:]:
            start_time = row[0]            
            if start_time >= used_room[0]:
                heapq.heappop(used_room)          
            heapq.heappush(used_room, row[1])
                
        return len(used_room)