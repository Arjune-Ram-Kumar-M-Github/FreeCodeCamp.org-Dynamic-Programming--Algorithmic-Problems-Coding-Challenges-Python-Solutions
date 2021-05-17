'''
Numbers	5	3	4				
Target	7						
0	1	2	3	4	5	6	7
[] None .. ..   ..  ..  ..  ..
[]  ..  .. [3]  [4] [5] [3 3]  [4 3]
 
Time Complexity - O(mn)
Space Complexity - O(m)

'''

def howSum(target,numbers):
    targetSum = [None]*(target+1)
    targetSum[0] = []

    for i in range(len(targetSum)):
        if targetSum[i] != None:
            for j in numbers:
                if i+j <= target:
                    temp = targetSum[i] + [j]
                    targetSum[i+j] = temp
    print(targetSum)
    return targetSum[target]

print(howSum(15,[2,3,5]))
    