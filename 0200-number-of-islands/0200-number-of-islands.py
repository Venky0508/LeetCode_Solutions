class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0

        def dfs(r,c):
            if (r,c) in visited:
                return

            visited.add((r,c))
            directions = [[1,0],[0,-1],[-1,0],[0,1]]

            for dr, dc in directions:
                if (r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == "1"):
                    dfs(r+dr, c+dc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    result += 1
        
        return result
