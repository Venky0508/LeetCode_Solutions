class Solution:
    def fib(self, n: int) -> int:
        return fibo(n)

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2) 