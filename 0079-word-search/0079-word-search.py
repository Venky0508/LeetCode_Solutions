class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or suffix[0] != board[row][col]:
                return False
            
            board[row][col] = '*'
            for m, n in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                if backtrack(row+m, col+n, suffix[1:]):
                    return True
            
            board[row][col] = suffix[0]
            return False
            
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, word):
                    return True
        return False