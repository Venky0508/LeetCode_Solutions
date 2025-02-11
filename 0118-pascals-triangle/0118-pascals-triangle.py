class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        result = [[1],[1,1]]
        count = len(result)

        while count < numRows:
            temp = [1]
            prev = result[-1]

            i = 0
            j = 1
            while j <= len(prev) - 1:
                total = prev[i] + prev[j]
                temp.append(total)
                i += 1
                j += 1
            
            temp.append(1)
            result.append(temp)
            count += 1

        return result