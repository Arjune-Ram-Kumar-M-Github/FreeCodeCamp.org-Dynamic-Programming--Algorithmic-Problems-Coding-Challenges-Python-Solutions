# Time Complexity - O(n^m)
# Space Complexity - O(m)
def canSum(targetSum,numbers):
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False
    
    for i in numbers:
        remainder = targetSum - i
        if (canSum(remainder,numbers)):
            return True

    return False

print(canSum(5,[1,2,3,4]))