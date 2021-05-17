# Time complextity - O(m*n)
# Space Complexitiy - o(m)

def canSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False
    
    for i in numbers:
        remainder = targetSum - i
        if (canSum(remainder,numbers,memo)):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


print(canSum(7,[2,4]))
# print(canSum(878979797,[5,4,3]))

