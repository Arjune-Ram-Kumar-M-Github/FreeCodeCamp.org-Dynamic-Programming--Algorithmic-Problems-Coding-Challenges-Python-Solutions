# time Complexity - O()
# Space Complexity - O()


def countConstruct(target,wordBank,memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    count = 0

    for i in wordBank:
        if target.startswith(i):
            newTarget=target.replace(i,"")
            if countConstruct(newTarget,wordBank,memo):
                count +=1
    memo[target] =  count
    return count
         
print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))
