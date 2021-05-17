# Time Complexity - O(n*m)
# Space Complexity - O(m)

def howSum(targetSum,numbers,memo={}):
    
    if targetSum in memo:
        return memo[targetSum]
       
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for i in numbers:
        remainder = targetSum - i

        combination = howSum(remainder,numbers)

        if combination != None:
            combination.append(i)
            memo[targetSum]=combination
            return memo[targetSum]

    return combination
            

print(howSum(5,[2,3,5]))