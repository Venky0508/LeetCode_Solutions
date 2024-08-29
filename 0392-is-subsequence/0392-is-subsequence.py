class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        n = len(s) - 1
        if s == '':
            return True
        if s == t:
            return False
        if t == '' and len(s) != 0:
            return False

        for i in range(len(t)):
            if s[check] == t[i]:
                if check == n:
                    return True
                check += 1
        
        return False


        