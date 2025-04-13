class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        word = ''
        for i in range(len(searchWord)):
            word += searchWord[i] 
            j = 0
            while j < len(products) :
                if word != products[j][:len(word)]:
                    products.pop(j)
                else:
                    j += 1
            
            if len(products) < 3:
                result.append(products)
            else:
                result.append(products[:3])

        return result
            