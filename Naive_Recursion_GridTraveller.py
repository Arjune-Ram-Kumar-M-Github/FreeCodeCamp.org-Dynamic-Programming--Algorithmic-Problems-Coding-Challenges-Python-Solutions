# Tiem Complexity - O(2^m+n)
# Space Complexity - O(n+m)

def gridTraveller(n,m):
    if n == 1 and m ==1:
        return 1

    if n==0 or m == 0:
        return 0

    return gridTraveller(n-1,m) + gridTraveller(n,m-1)

     