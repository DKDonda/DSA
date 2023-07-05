class Solution:
    def fib(self, n: int) -> int:
        ### This is using concept of Memoization.
        mem = [0,1]
        if n == 0: return 0
        if n == 1: return 1
        else:
            for i in range(1,n):
                mem.append(mem[i]+mem[i-1])
            return mem[n]