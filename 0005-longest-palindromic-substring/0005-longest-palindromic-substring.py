class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                temp = s[i:j]
                rev = temp[::-1]
                if temp == rev:
                    ans.append((temp, len(temp)))

        
        ans = sorted(ans, key = lambda x:x[1])
        if ans == []:
            return ""
        else:
            result = ans[-1]
            return result[0]