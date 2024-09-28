class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        if numRows == 1:
            return s
        
        for i in range(numRows):
            ans.append([])
            
            
        i = 0
        j = 0
        flag = True
        while i < len(s):
            if flag == True:
                if j == numRows - 1:
                    flag = False
                    ans[j].append(s[i])
                    j -= 1
                else:
                    ans[j].append(s[i])
                    j += 1
                    
            else:
                if j == 0:
                    flag = True
                    ans[j].append(s[i])
                    j += 1
                else:
                    ans[j].append(s[i])
                    j -= 1
                  
            i += 1
        
        result = ''
        for sub in ans:
            for ch in sub:
                result += ch
                
        return result
        