class Solution:
    def reverseVowels(self, s: str) -> str:
        # ans = ''
        chars = []
        # pos = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         chars.append(s[i])
        #         pos.append(i)
        
        # index = len(chars) - 1
        # for x in range(len(s)):
        #     if x in pos:
        #         ans += chars[index]
        #         index -= 1
        #     else:
        #         ans += s[x]

        # return ans
        revStr = s[::-1]
        for i in revStr:
            if i in vowels:
                chars.append(i)
        
        ans = ''
        for j in s:
            if j not in vowels:
                ans += j
            else:
                ans += chars[0]
                if len(chars) != 1:
                    chars = chars[1:]
        
        return ans

        
        