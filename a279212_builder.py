from boolean_list_to_file import BitmapWriter

class A279212Builder: 
    def __init__(self, n):
        self.n = 2**n
        self.grid = []
        self.initialize_grid()
        self.initialize_parity_lists()
        self.fill_grid()

    def initialize_parity_lists(self):
        self.column_parity       = [False] * self.n
        self.row_parity          = [False] * (4*self.n)
        self.row_parity[0]       = True
        self.row_parity[1]       = True
        self.top_diagonal_parity = [False] * (4*self.n)
        self.diagonal_parity     = [False] * (4*self.n)
        self.diagonal_parity[0]  = True
        self.diagonal_parity[1]  = True
        self.antidiagonal_parity = False

    def initialize_grid(self):
        for _ in range(4*self.n):
            self.grid.append([False] * self.n)
        self.grid[0][0] = True
        self.grid[1][0] = True
        self.grid[0][1] = False

    def fill_grid(self):
        for i in range(2,4*self.n): 
            self.antidiagonal_parity = False
            for j in range(i+1):
                if j >= self.n:
                    break
                if i-j >= j:
                    self.grid[i-j][j]           = self.column_parity[j] ^ self.row_parity[i-j] ^ self.antidiagonal_parity ^ self.diagonal_parity[i - 2*j]
                    # adjust the helper sums
                    self.antidiagonal_parity    = (self.antidiagonal_parity ^ self.grid[i-j][j])
                    self.diagonal_parity[i-2*j] = (self.diagonal_parity[i-2*j] ^ self.grid[i-j][j])
                    self.column_parity[j]       = (self.column_parity[j] ^ self.grid[i-j][j])
                    self.row_parity[i-j]        = (self.row_parity[i-j] ^ self.grid[i-j][j])
                else:
                    self.grid[i-j][j]               = self.column_parity[j] ^ self.row_parity[i-j] ^ self.antidiagonal_parity ^ self.top_diagonal_parity[2*j-i]
                    # adjust the helper sums
                    self.antidiagonal_parity        = (self.antidiagonal_parity ^ self.grid[i-j][j])
                    self.top_diagonal_parity[2*j-i] = (self.top_diagonal_parity[2*j-i] ^ self.grid[i-j][j])
                    self.column_parity[j]           = (self.column_parity[j] ^ self.grid[i-j][j])
                    self.row_parity[i-j]            = (self.row_parity[i-j] ^ self.grid[i-j][j])
    
    def truncated_grid(self):
        return self.grid[0:2*self.n]

BitmapWriter(A279212Builder(8).truncated_grid()).write_bitmap("A279212_8.bmp")