class Solution:
    def isValid(self, s: str) -> bool:
        op = ["[", "{", "("]
        seen = []
        for i in s:
            if i in op:
                seen.append(i)
            else:
                if seen == []:
                    return False              
                elif i == "]":
                    check = seen[-1]
                    if check == "[":
                        seen.pop()
                    else:
                        return False
                elif i == "}":
                    check = seen[-1]
                    if check == "{":
                        seen.pop()
                    else:
                        return False
                else:
                    check = seen[-1]
                    if check == "(":
                        seen.pop()
                    else:
                        return False
                
        if seen != []:
            return False
        return True