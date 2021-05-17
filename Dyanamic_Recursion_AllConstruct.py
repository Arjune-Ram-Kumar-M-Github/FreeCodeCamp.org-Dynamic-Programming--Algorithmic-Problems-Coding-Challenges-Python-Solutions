# time Complexity - O(n^m*m)
# Space Complexity - O(m^2)

def addSuffix(suffixWays,suffix):
    for i in suffixWays:
        i.append(suffix)

    return suffixWays



def countConstruct(target,wordBank,memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for i in wordBank:
        if target.startswith(i):
            newTarget=target.replace(i,"")
            suffixWays = countConstruct(newTarget,wordBank,memo)
            if len(suffixWays) >0:
                temp = addSuffix(suffixWays,i)
                for suffix in temp:
                    result.append(suffix)
    memo[target] =  result        
    return result

         
print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))
