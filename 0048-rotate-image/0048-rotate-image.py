class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        n = len(matrix)
        
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i == n - 1:
                    temp.append([matrix[i][j]])
                else:
                    temp[j].append(matrix[i][j])
                    
        for x in range(n):
            for y in range(n):
                matrix[x][y] = temp[x][y]
                    