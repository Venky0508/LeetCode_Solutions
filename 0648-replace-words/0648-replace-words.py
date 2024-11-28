class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tokens = sentence.split(' ')
        result = ''
        for word in tokens:
            flag = False
            for i in range(len(word)):
                root = word[:i]
                if root in dictionary:
                    result += root + " "
                    flag = True
                    break
            if flag == False:
                result += word + " "
        
        result = result.strip()
        return result