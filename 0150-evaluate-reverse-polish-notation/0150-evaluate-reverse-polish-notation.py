class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '/', '*']
        
        for token in tokens:
            if token not in operators:
                num = int(token)
                stack.append(num)
            else:
                first = stack.pop()
                second = stack.pop()
                if token == '+':
                    val = first + second
                    stack.append(val)
                elif token == '-':
                    val = second - first
                    stack.append(val)
                elif token == '*':
                    val = first * second
                    stack.append(val)
                else:
                    val = second / first
                    stack.append(int(val))
        
        ans = stack.pop()
        return ans