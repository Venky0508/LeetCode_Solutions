class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        
        edge1 = edges[0]
        edge2 = edges[1]
        
        if edge1[0] in edge2:
            common = edge1[0]
        else:
            common = edge1[1]

        return common
        