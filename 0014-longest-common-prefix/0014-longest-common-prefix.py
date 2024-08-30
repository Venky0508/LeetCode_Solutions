class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            new = strs[i]
            if prefix == new:
                continue
            if prefix == '':
                return ''
            else:
                for j in range(len(prefix), -1, -1):
                    if prefix[:j] == new[:j]:
                        prefix = prefix[:j]
                        break
                    elif j == 0:
                        return ''
                    else:
                        continue
        
        return prefix
                    
                    
                        
        