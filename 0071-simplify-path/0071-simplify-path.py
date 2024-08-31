class Solution:
    def simplifyPath(self, path: str) -> str:
#         temp = path.strip().split('/')
#         print(temp)
#         ans = '/'
#         for t in range(len(temp)):
#             if temp[t] == '' or temp[t] == '..' or temp[t] == '.' :
#                 continue
#             elif t+1 != len(temp) and temp[t+1] == '..':
#                 continue
#             else:
#                 ans += temp[t] + '/'
        
#         if ans != '/':
#             ans = ans[:-1]
#         return ans
        dirOrFiles = []
        path = path.split("/")
        for elem in path:
            if dirOrFiles and elem == "..":
                dirOrFiles.pop()
            elif elem not in [".", "", ".."]:
                dirOrFiles.append(elem)
                
        return "/" + "/".join(dirOrFiles)
        
        