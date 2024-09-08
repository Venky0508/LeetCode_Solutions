class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        seen = []
        i = 0
        if len(matrix) == 1:
            for j in matrix[0]:
                if target == j:
                    return True
                else:
                    continue
            return False
        
        
        
        while i < len(matrix):
            if i == 0:
                check = matrix[i][0]
                if target < check:
                    return False
                seen.append((check,i))
                i += 1
                
            elif i == len(matrix) - 1:
                prev, index = seen[-1]
                curr = matrix[i][0]
                if target > curr:
                    for j in matrix[i]:
                        if target == j:
                            return True
                        else:
                            continue
                    return False
                elif target < curr:
                    for j in matrix[index]:
                        if target == j:
                            return True
                        else:
                            continue
                    return False
                elif target == curr:
                    return True
                
                
            else:
                prev, index = seen[-1]
                curr = matrix[i][0]
                if target > curr:
                    seen.append((curr, i))
                    i += 1
                elif target < curr:
                    for j in matrix[index]:
                        if target == j:
                            return True
                        else:
                            continue
                    return False
                elif target == curr:
                    return True
                            
                            
                    
        