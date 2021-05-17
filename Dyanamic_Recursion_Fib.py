# Tiime Complxity - O(2n) ~ O(n)
# Space Complexity - O(n)

import time

def fib(n,memo={}):
    if n in memo:
        return memo[n]

    if n<2:
        return n

    memo[n] = fib(n-1,memo) + fib(n-2,memo)

    return memo[n]

startTime = time.time()
print(fib(5))
stopTime = time.time()

print(stopTime-startTime)

startTime = time.time()
print(fib(10))
stopTime = time.time()

print(stopTime-startTime)

startTime = time.time()
print(fib(15))
stopTime = time.time()

print(stopTime-startTime)

startTime = time.time()
print(fib(30))
stopTime = time.time()

print(stopTime-startTime)

    