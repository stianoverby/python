''' 509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Constraints:
0 <= n <= 30

Source: https://leetcode.com/problems/fibonacci-number/
'''
    

class Solution(object):

    def fibonacci(self, n):
        # Iterative solution

        if n == 0: return 0
        if n == 1: return 1

        fib_sequence = [0 for _ in range(n+1)]
        fib_sequence[1] = 1

        for i in range( len(fib_sequence) - 2 ):
            # set every element besides the two first, to be the sum
            # of the two previous elements.
            fib_sequence[i+2] = fib_sequence[i] + fib_sequence[i+1]
    
        return fib_sequence[n]