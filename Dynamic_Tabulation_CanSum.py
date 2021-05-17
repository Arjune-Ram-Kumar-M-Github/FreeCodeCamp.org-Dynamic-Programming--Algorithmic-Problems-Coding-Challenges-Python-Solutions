'''
Numbers	5	3	4				
Target	7						
0	1	2	3	4	5	6	7
TRUE	FALSE	FALSE	FALSE	FALSE	FALSE	FALSE	FALSE
TRUE	FALSE	FALSE	TRUE	TRUE	TRUE	TRUE	TRUE

Time Complexity - O(mn)
Space Complexity - O(m)

'''

def canSum(target,numbers):
    targetSum = [False]*(target+1)
    targetSum[0] = True

    for i in range(len(targetSum)):
        for j in numbers:
            if targetSum[i] == True:
                if i+j <= target:
                    targetSum[i+j] = True

    print(targetSum)

    return targetSum[target]

# print(canSum(15,[5,4,3]))
    