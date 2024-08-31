class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for i in strs:
            temp = sorted(i)
            key = tuple(temp)
            if key not in wordMap:
                wordMap[key] = []
            wordMap[key].append(i)
            
        ans = []
        for val in wordMap.values():
            ans.append(val)
            
        return ans
            
        
            
            
            
        