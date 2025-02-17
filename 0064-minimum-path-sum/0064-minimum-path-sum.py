class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         if m-1 == 0:
#             return sum(grid[0])
        
#         src = [0, 0]
#         des = [m-1, n-1]
#         return dfs(grid, src , des)

# def dfs(grid, curr, dest):
#     if curr[0] == dest[0] and curr[1] == dest[1]:
#         return grid[dest[0]][dest[1]]
#     else:
#         if curr[0] + 1 < len(grid) and curr[1] + 1 < len(grid[0]):
#             return min(grid[curr[0]][curr[1]] + dfs(grid, [curr[0]+1,curr[1]], dest), grid[curr[0]][curr[1]] + dfs(grid, [curr[0],curr[1]+1], dest))
#         elif curr[0] + 1 == len(grid):
#             return grid[curr[0]][curr[1]] + dfs(grid, [curr[0],curr[1]+1], dest)
#         else:
#             return grid[curr[0]][curr[1]] + dfs(grid, [curr[0]+1,curr[1]], dest)

        m, n = len(grid), len(grid[0])
        cur = [grid[0][0]] * m
        
        for i in range(1, m):
            cur[i] = cur[i - 1] + grid[i][0]
        
        for j in range(1, n):
            cur[0] += grid[0][j]
            for i in range(1, m):
                cur[i] = min(cur[i - 1], cur[i]) + grid[i][j]
        
        return cur[m - 1]