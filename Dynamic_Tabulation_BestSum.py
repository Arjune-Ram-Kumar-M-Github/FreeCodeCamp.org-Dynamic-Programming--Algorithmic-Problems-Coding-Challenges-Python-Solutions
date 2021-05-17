'''
Numbers	5	3	4				
Target	7						
0	1	2	3	4	5	6	7
[] None .. ..   ..  ..  ..  ..
[]  ..  .. [3]  [4] [5] [3 3]  [4 3]
 
Time Complexity - O(mn)
Space Complexity - O(m)

'''

def bestSum(target,numbers):
    targetSum = [None]*(target+1)
    targetSum[0] = []

    for i in range(len(targetSum)):
        for j in numbers:
            if targetSum[i] != None:
                if i+j <= target:
                    temp = targetSum[i] + [j]
                    if targetSum[i+j] == None:
                        targetSum[i+j] = temp
                    else:
                        if len(temp) < len(targetSum[i+j]):
                            targetSum[i+j] = temp

    return targetSum[target]

print(bestSum(15,[1,2,5,7,8]))    