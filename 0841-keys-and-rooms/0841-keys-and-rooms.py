class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # n = len(rooms)
        # key = set()
        # for i in range(len(rooms)):
        #     if i == 0:
        #         for k in rooms[i]:
        #             key.add(k)
                
        #     else:
        #         if i in key:
        #             for k in rooms[i]:
        #                 key.add(k)
        #         elif rooms[i] == []:
        #             continue
        #         else:
        #             return False
        
        # return True

        # n = len(rooms)
        # keys = {}

        # for i in range(n):
        #     key = rooms[i]
        #     for j in key:
        #         if j not in keys:
        #             keys[j] = []
        #         keys[j].append(i)
        
        # for k,v in keys.items():
        #     if k != 0:
        #         flag = False
        #         for val in v:
        #             if val < k:
        #                 flag = True
        #                 break
        #         if flag == False:
        #             return flag
        # return True
        visited = set()

        def dfs(room_key):
            visited.add(room_key)
            for key in rooms[room_key]:
                if key not in visited:
                    dfs(key)
        
        dfs(0)
        return len(visited) == len(rooms)
                    
                 
        