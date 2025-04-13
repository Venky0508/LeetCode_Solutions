class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if not board or not board[0]:
        #     return

        # rows = len(board)
        # cols = len(board[0])
        # visited = set()

        # def dfs(r, c):
        #     if (r, c) in visited:
        #         return
            
        #     visited.add((r, c))
        #     directions = [[1,0],[0,-1],[-1,0],[0,1]]

        #     for dr, dc in directions:
        #         nr = r+dr
        #         nc = c+dc

        #         if nr > 0 and nr < rows-1 and nc > 0 and nc < cols-1 and board[nr][nc] == "O":
        #             board[nr][nc] = "X" 
        #             dfs(nr, nc)

        # for r in range(1, rows-1):
        #     for c in range(1, cols-1):
        #         if (r,c) not in visited and board[r][c] == "O":
        #             board[r][c] = "X"
        #             dfs(r,c)

        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            """Mark all boundary-connected 'O's as safe ('S')."""
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'S'  # Temporarily mark as safe
                dfs(r + 1, c)  # Down
                dfs(r - 1, c)  # Up
                dfs(r, c + 1)  # Right
                dfs(r, c - 1)  # Left

        # Step 1: Mark all 'O's connected to the border as safe ('S')
        for r in range(rows):
            for c in [0, cols - 1]:  # First & Last column
                if board[r][c] == 'O':
                    dfs(r, c)

        for c in range(cols):
            for r in [0, rows - 1]:  # First & Last row
                if board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Convert remaining 'O's to 'X' and revert 'S' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':  # Surrounded regions
                    board[r][c] = 'X'
                elif board[r][c] == 'S':  # Restore safe 'O's
                    board[r][c] = 'O'



