class TableArray:
    def __init__(self, table_sequence, int_to_bool_function):
        self.int_to_bool_function = int_to_bool_function
        self.sequence = table_sequence
        self.initialize_boolean_grid()
        self.fill_boolean_grid()

    def size_of_table(self):
        k = 1
        while (k*(k+1))//2 < len(self.sequence):
            k+=1
        return k

    def initialize_boolean_grid(self):
        self.grid = []
        table_size = self.size_of_table()
        for _ in range(table_size):
            self.grid.append([False] * table_size)

    def fill_boolean_grid(self):
        i = 0
        j = 0
        for (_,a_n) in self.sequence:
            self.grid[i][j] = self.int_to_bool_function(a_n)
            if i == 0:
                i = j + 1
                j = 0
            else:
                i -= 1
                j += 1
