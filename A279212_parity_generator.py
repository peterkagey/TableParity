n = 8
grid = []
for i in range(n):
    grid.append([False] * n)
grid[0][0] = True
grid[1][0] = True
grid[0][1] = False

column_parity = [False] * n
row_parity = [False] * n
row_parity[0] = True
row_parity[1] = True
top_diagonal_parity = [False] * (2*n)
diagonal_parity = [False] * (2*n)
diagonal_parity[0] = True
diagonal_parity[1] = True
antidiagonal_parity = False

for i in range(2,n): 
    antidiagonal_parity = False
    for j in range(i+1):
        if i-j >= j:
            # calculate sum
            grid[i-j][j] = column_parity[j] ^ row_parity[i-j] ^ antidiagonal_parity ^ diagonal_parity[i - 2*j]
            # adjust the helper sums
            antidiagonal_parity = (antidiagonal_parity ^ grid[i-j][j])
            diagonal_parity[i-2*j] = (diagonal_parity[i-2*j] ^ grid[i-j][j])
            column_parity[j] = (column_parity[j] ^ grid[i-j][j])
            row_parity[i-j] = (row_parity[i-j] ^ grid[i-j][j])
        else:
            # calculate sum
            grid[i-j][j] = column_parity[j] ^ row_parity[i-j] ^ antidiagonal_parity ^ top_diagonal_parity[2*j-i]
            # adjust the helper sums
            antidiagonal_parity = (antidiagonal_parity ^ grid[i-j][j])
            top_diagonal_parity[2*j-i] = (top_diagonal_parity[2*j-i] ^ grid[i-j][j])
            column_parity[j] = (column_parity[j] ^ grid[i-j][j])
            row_parity[i-j] = (row_parity[i-j] ^ grid[i-j][j])

print(grid)