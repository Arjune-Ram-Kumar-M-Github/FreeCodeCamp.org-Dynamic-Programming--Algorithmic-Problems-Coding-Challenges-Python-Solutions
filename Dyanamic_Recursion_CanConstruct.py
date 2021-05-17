# Time Complexity - O(n*m*m)
# Space Complexity - O(m^2)

def canConstruct(word,wordArray,memo={}):
    if word in memo:
        return memo[word]

    if word == '':
        return True

    for i in wordArray:
        if word.startswith(i):
            newWord = word.replace(i,'')
            if (canConstruct(newWord,wordArray,memo)):
                memo[newWord] = True
                return True
    memo[word] = False
    return False

print(canConstruct('abcdef',['ab','abc','cd','df','abcd']))