import math
from spiral_calculator import SpiralCalculator

class PlaneBuilder:
    def __init__(self, integer_sequence, int_to_bool_function):
        self.int_to_bool_function = int_to_bool_function
        self.sequence = integer_sequence
        self.initialize_boolean_grid()
        self.fill_boolean_grid()

    def initialize_boolean_grid(self):
        self.grid = []
        table_size = self.size_of_table()
        for _ in range(table_size):
            self.grid.append([False] * table_size)

    def size_of_table(self):
        raise NotImplementedError

    def fill_boolean_grid(self):
        raise NotImplementedError

class TableBuilder(PlaneBuilder):

    def size_of_table(self):
        k = 1
        while (k*(k+1))//2 < len(self.sequence):
            k+=1
        return k

    def fill_boolean_grid(self):
        i = 0
        j = 0
        for (_,a_n) in self.sequence:
            self.grid[i][j] = self.int_to_bool_function(a_n)
            if i == 0:
                (i, j) = (j + 1, 0)
            else:
                (i, j) = (i - 1, j + 1)

class SpiralBuilder(PlaneBuilder):
    spiral_calculator = SpiralCalculator()

    def size_of_table(self):
        return math.ceil(math.sqrt(len(self.sequence)))

    def center_of_table(self):
        n = self.size_of_table()
        if n % 2 == 0:
            return (n//2, n//2 - 1)
        else:
            return ((n-1)//2, (n-1)//2)

    def initialize_boolean_grid(self):
        self.center = self.center_of_table()
        super().initialize_boolean_grid()

    def fill_boolean_grid(self):
        counter = 1
        (i,j) = self.center
        for (_,a_n) in self.sequence:
            y = self.spiral_calculator.a174344(counter)
            x = self.spiral_calculator.a274923(counter)
            self.grid[i-x][j+y] = self.int_to_bool_function(a_n)
            counter += 1
