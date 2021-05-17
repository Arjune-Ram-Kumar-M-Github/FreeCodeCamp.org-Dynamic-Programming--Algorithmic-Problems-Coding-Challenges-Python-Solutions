def fib(n):
    fibArr = [0,1]

    for i in range(2,n+1):
        fibArr.append(fibArr[i-1]+fibArr[i-2])

    return fibArr[n]

print(fib(10))