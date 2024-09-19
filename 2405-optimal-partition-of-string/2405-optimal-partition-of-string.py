class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        substrings = []
        temp = ''
        
        while i < len(s):
            if s[i] not in temp:
                temp += s[i]
            else:
                substrings.append(temp)
                temp = s[i]
            
            i += 1
        
        if temp != '':
            substrings.append(temp)
            
        return len(substrings)
        