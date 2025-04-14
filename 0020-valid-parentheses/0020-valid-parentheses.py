class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_Open = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for c in s:
            if c in close_to_Open:
                if stack and stack[-1] == close_to_Open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

        