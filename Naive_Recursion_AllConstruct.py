# time Complexity - O(n^m*m)
# Space Complexity - O(m^2)

def addSuffix(suffixWays,suffix):
    for i in suffixWays:
        i.append(suffix)

    return suffixWays



def countConstruct(target,wordBank):
    
    if target == "":
        return [[]]

    result = []

    for i in wordBank:
        if target.startswith(i):
            newTarget=target.replace(i,"")
            suffixWays = countConstruct(newTarget,wordBank)
            if len(suffixWays) >0:
                temp = addSuffix(suffixWays,i)
                for suffix in temp:
                    result.append(suffix)
            
    return result

         
print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))
