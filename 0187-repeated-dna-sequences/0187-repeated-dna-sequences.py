class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        j = 10
        frequencyMap = {}

        if len(s) <= 10:
            return []
        
        result = []
        while j <= len(s):
            temp = s[i:j]
            if temp not in frequencyMap:
                frequencyMap[temp] = 1
            else:
                frequencyMap[temp] += 1
                if frequencyMap[temp] == 2:
                    result.append(temp)

            i += 1
            j += 1

        return result