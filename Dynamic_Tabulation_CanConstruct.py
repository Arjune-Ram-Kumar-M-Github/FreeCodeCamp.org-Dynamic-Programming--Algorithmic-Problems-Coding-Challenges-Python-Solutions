def canConstruct(word,wordArray):
    table = [False]*(len(word)+1)
    table[0] = True
     

    for i in range(len(table)):
        if table[i] == True:
            for j in wordArray:
                if word[i:].startswith(j):
                    if i + len(j) <= len(word):
                        table[i + len(j)] = True

    # print(table)

    return table[len(word)]

print(canConstruct('abcdef',['ab','abc','cd','df','abcd']))
