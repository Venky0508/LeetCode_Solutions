class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp.append(matrix[i][j])
                if len(temp) == k:
                    return temp[-1]