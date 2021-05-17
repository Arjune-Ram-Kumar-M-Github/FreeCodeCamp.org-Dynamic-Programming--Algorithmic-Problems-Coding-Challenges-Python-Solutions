# Tiem Complexity - O(m+n)
# Space Complexity - O(n+m)

def gridTraveller(n,m,memo = {}):

    key = str(n) + ',' + str(m)

    if key in memo:
        return memo[key]

    if n == 1 and m ==1:
        return 1

    if n==0 or m == 0:
        return 0

    memo[key] = gridTraveller(n-1,m) + gridTraveller(n,m-1)
    

    return memo[key]

print(gridTraveller(50,50))