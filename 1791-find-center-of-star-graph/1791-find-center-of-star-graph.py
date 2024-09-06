class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        
        edge1 = edges[0]
        edge2 = edges[1]
        
        if edge1[0] in edge2:
            common = edge1[0]
        else:
            common = edge1[1]
            
        if n > 2:
            for i in range(2,n):
                check = edges[i]
                if common in check:
                    continue
        return common
        