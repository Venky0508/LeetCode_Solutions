class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        cols = {}
        total = len(grid)

        for i in range(total):
            rows[i] = grid[i]
            if i not in cols:
                cols[i] = []
            for j in range(total):
                if j not in cols:
                    cols[j] = []
                    cols[j].append(grid[i][j])
                else:
                    cols[j].append(grid[i][j])
        
        count = 0
        for val1 in rows.values():
            for val2 in cols.values():
                if val1 == val2:
                    count += 1
        
        return count


        
        