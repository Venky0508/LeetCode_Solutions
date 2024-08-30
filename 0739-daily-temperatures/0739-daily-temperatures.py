class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = []
#         for i in range(len(temperatures)):
#             if i+1 != len(temperatures):
#                 j = i + 1
#                 count = 1
#                 while temperatures[j] <= temperatures[i]:
#                     j += 1
#                     count += 1
#                     if j == len(temperatures):
#                         count = 0
#                         break
                    
#                 answer.append(count)
                           
#             else:
#                 answer.append(0)
        
#         return answer
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack == []:
                stack.append((i, temperatures[i]))
            else:
                prev_index, stack_top = stack[-1]
                curr_index, curr_val = i, temperatures[i]
                while curr_val > stack_top:
                    answer[prev_index] = curr_index - prev_index
                    stack.pop()
                    if len(stack) != 0:
                        prev_index, stack_top = stack[-1]
                    else:
                        break
                    
                stack.append((curr_index, curr_val))
            
        return answer
            