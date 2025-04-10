class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        stack = []
        prev = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                stack.pop()

            if len(stack) == 0:
                ans.append(s[prev:i+1])
                prev = i+1
        
        result = ""
        for temp in ans:
            if len(temp) > 2:
                new = temp[1:len(temp)-1]
                result += new

        return result

                
