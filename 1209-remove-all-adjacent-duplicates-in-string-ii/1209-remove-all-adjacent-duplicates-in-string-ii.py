class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack = []

        # for i in s:
        #     stack.append(i)
        #     if len(stack) >= k:
        #         temp = stack[-k:]
        #         flag = True
        #         for i in range(1, len(temp)):
        #             if temp[i] != temp[0]:
        #                 flag = False
        #                 break
                
        #         if flag == True:
        #             stack = stack[:-k]

        # return "".join(stack)

        stack = []

        for i in s:
            if len(stack) > 0 and i == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i, 1])

        ans = ""
        for char,n in stack:
            ans += char * n

        return ans
