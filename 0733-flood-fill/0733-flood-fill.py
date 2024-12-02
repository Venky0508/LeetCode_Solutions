class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(image)
        cols = len(image[0])
        result = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(image[i][j])
            result.append(temp)
                
        visited = set()
        need_to_visit = [(sr, sc)]
        
        while need_to_visit:
            r, c = need_to_visit.pop()
            
            if (r, c) not in visited:
                result[r][c] = color
                check = image[r][c]
                neighbors = [(r+dirr[0], c+dirr[1]) for dirr in directions]

                for val in neighbors:
                    x, y = val
                    if x < rows and x >= 0 and y < cols and y >= 0:
                        if image[x][y] == check:
                            need_to_visit.append((x, y))
                        
                visited.add((r, c))
                    
        return result
                
            
                        
                
