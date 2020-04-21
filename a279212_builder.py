from boolean_list_to_file import BitmapWriter

class A279212Builder:
    def __init__(self, n):
        self.n = 2**n
        self.grid = []
        self.initialize_grid()
        self.initialize_parity_lists()
        self.fill_grid()

    def initialize_parity_lists(self):
        self.column_parity          = [False] * self.n
        self.column_parity[0]       = True
        self.row_parity             = [False] * (3*self.n)
        self.row_parity[0]          = True
        self.top_diagonal_parity    = [False] * (self.n)
        self.sub_diagonal_parity    = [False] * (3*self.n)
        self.sub_diagonal_parity[0] = True
        self.antidiagonal_parity    = False

    def initialize_grid(self):
        for _ in range(3*self.n):
            self.grid.append([False] * self.n)

    def fill_grid(self):
        self.grid[0][0] = True
        for i in range(1, 3*self.n):
            self.antidiagonal_parity = False
            for j in range(min(i+1, self.n)):
                if i-j >= j:
                    self.update_below_diagonal(i, j)
                else:
                    self.update_above_diagonal(i, j)

    def update_below_diagonal(self, i, j):
        self.grid[i-j][j]               = self.column_parity[j] ^ self.row_parity[i-j] ^ self.antidiagonal_parity ^ self.sub_diagonal_parity[i - 2*j]
        self.sub_diagonal_parity[i-2*j] ^= self.grid[i-j][j]
        self.update_parities(i, j)

    def update_above_diagonal(self, i, j):
        self.grid[i-j][j]               = self.column_parity[j] ^ self.row_parity[i-j] ^ self.antidiagonal_parity ^ self.top_diagonal_parity[2*j-i]
        self.top_diagonal_parity[2*j-i] ^= self.grid[i-j][j]
        self.update_parities(i, j)

    def update_parities(self, i, j):
        self.antidiagonal_parity ^= self.grid[i-j][j]
        self.column_parity[j]    ^= self.grid[i-j][j]
        self.row_parity[i-j]     ^= self.grid[i-j][j]

    def truncated_grid(self):
        return self.grid[0:2*self.n]

BitmapWriter(A279212Builder(10).truncated_grid()).write_bitmap("A279212_10.bmp")
