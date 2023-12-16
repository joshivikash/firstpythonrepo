def final(n, moves):
    """
    Compute the final position
    
    Argument:
        n: int
        moves: string
    Return:
        (x, y): tuple
    """
    mat = [[(i+1,j+1) for j in range(n)] for i in range(n)]
    i,j=0,0
    for m in moves:
        if m == 'N':
            j = j + 1 if j + 1 < n else j
        if m == 'E':
            i = i + 1 if i + 1 < n else i
        if m == 'W':
            i = i - 1 if i - 1 > -1 else i
        if m == 'S':
            j = j - 1 if j - 1 > -1 else j
    return mat[i][j]

print(final(10,'NNNEENSNENESNEWNSWENENSENWNSSSNWENESNESEW'))