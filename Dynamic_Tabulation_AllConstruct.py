def addSuffix(suffixArray,suffix):
    temp = []
    if len(suffixArray) !=0:
        for i in suffixArray:
            temp += [i] + [suffix]
    else:
        temp += [suffix]
    return temp


    


def allConstruct(word,wordArray):
    table = [None]*(len(word)+1)
    table[0] = []
     

    for i in range(len(table)):
        if table[i] != None:
            for j in wordArray:
                if word[i:].startswith(j):
                    if i + len(j) <= len(word):
                        temp =  addSuffix(table[i],j)
                        if table[i+len(j)] == None:
                            table[i + len(j)] = temp
                        else:
                            table[i+len(j)].append(temp)

    print(table)

    return table[len(word)]


print(allConstruct('abcdef',['ab','abc','cd','def','abcd']))
