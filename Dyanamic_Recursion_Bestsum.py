# Time Complexity - O(m*n)
# Space Complexity - O(m)


def bestSum(targetNumber,numbers,memo={}):

    if targetNumber in memo:
        return memo[targetNumber]
    if targetNumber == 0:
        return []

    if targetNumber < 0:
        return None

    shortestCombination = None

    for i in numbers:

        remainder = targetNumber - i
        combination = bestSum(remainder,numbers) 

        if combination != None:
            combination.append(i)
            if (shortestCombination == None) or (len(shortestCombination) > len(combination)):
                shortestCombination = combination
            
        
    memo[targetNumber] = shortestCombination
            
    return shortestCombination


print(bestSum(100,[5,3,4,7]))

