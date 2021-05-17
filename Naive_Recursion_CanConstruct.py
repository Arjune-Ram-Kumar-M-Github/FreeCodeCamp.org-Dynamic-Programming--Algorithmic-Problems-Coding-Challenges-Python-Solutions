# Time Complexity - O(n^m*m)
# Space Complexity - O(m^2)

def canConstruct(word,wordArray):

    if word == '':
        return True

    for i in wordArray:
        if word.startswith(i):
            newWord = word.replace(i,'')
            if (canConstruct(newWord,wordArray)):
                return True

    return False

print(canConstruct('abcdef',['ab','abc','cd','df','abcd']))