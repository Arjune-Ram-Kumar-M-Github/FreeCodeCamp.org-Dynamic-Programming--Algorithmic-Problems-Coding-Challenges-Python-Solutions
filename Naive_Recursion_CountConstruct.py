# time Complexity - O(n^m*m)
# Space Complexity - O(m^2)


def countConstruct(target,wordBank):
    
    if target == "":
        return 1

    count = 0

    for i in wordBank:
        if target.startswith(i):
            newTarget=target.replace(i,"")
            if countConstruct(newTarget,wordBank):
                count +=1

    return count
         
print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))
