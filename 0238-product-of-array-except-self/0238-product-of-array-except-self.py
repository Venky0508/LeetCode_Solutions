import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        pre = 1
        post = 1

        for i in range(n):
            answer[i] = pre
            pre *= nums[i]

        for j in range(n-1, -1, -1):
            answer[j] *= post
            post *= nums[j]

        return answer

        # for i in range(len(nums)):
        #     temp = nums[:i] + nums[i+1:]
        #     res = np.array(temp)
        #     ans = np.prod(res)
        #     answer.append(int(ans))
        
        # return answer