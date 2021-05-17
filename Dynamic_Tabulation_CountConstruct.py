def countConstruct(word,wordArray):
    table = [0]*(len(word)+1)
    table[0] = 1
     

    for i in range(len(table)):
        if table[i] !=0:
            for j in wordArray:
                if word[i:].startswith(j):
                    if i + len(j) <= len(word):
                        table[i + len(j)] +=1

    print(table)

    return table[len(word)]

print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('purple',['purp','p','ur','le','purpl']))

