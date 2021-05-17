'''
GridTraveller(3,3) -> 6
0	0	0	0
0	1	1	1
0	1	2	3
0	1	3	6

'''


def gridTraveller(m,n):
    table = [[0]*(n+1) for i in range(m+1)]
    table[1][1]= 1

    for i in range(m+1):
        for j in range(n+1):
            Current = table[i][j]

            if j+1 <= n:
                table[i][j+1] +=Current
            if i+1 <= m:
                table[i+1][j] += Current

    return table[m][n]

print(gridTraveller(3,3))

