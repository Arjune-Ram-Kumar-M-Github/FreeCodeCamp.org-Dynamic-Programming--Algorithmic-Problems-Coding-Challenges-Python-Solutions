# Time Complexity - O(n^m)
# Space Complexity - O(m)

def howSum(targetSum,numbers):
    
    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for i in numbers:
        remainder = targetSum - i

        combination = howSum(remainder,numbers)

        if combination != None:
            combination.append(i)
            return combination

    return combination
            

print(howSum(50,[2,3,5,7]))