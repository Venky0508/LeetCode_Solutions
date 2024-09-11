class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        temp = [[1] * n] * m
        
        for i in range(m):
            s = matrix[i]
            if 0 in s:
                temp[i] = [0] * n
                for j in range(n):
                    if matrix[i][j] == 0:
                        x = 0
                        while x < m:
                            temp[x][j] = 0
                            x += 1
                            
        for a in range(m):
            for b in range(n):
                if temp[a][b] == 0:
                    matrix[a][b] = 0
         