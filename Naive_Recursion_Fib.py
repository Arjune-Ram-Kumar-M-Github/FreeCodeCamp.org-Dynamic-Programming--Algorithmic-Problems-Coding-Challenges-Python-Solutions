# Time Complexity - O(2^n)
# Space Complexity - O(n)

import time

def fib(n):
    if n<2:
        return n

    return fib(n-1) + fib(n-2)

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
