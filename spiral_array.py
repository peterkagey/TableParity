import math
from spiral_calculator import SpiralCalculator

class SpiralArray:
    def __init__(self, spiral_sequence, int_to_bool_function):
        self.int_to_bool_function = int_to_bool_function
        self.spiral_calculator = SpiralCalculator()
        self.sequence = spiral_sequence
        self.center = self.center_of_table()
        self.initialize_boolean_grid()
        self.fill_boolean_grid()

    def size_of_table(self):
        return math.ceil(math.sqrt(len(self.sequence)))

    def center_of_table(self):
        n = self.size_of_table()
        if n % 2 == 0:
            return (n//2, n//2 - 1)
        else:
            return ((n-1)//2, (n-1)//2)

    def initialize_boolean_grid(self):
        self.grid = []
        table_size = self.size_of_table()
        for _ in range(table_size):
            self.grid.append([False] * table_size)

    def fill_boolean_grid(self):
        counter = 1
        (i,j) = self.center_of_table()
        for (_,a_n) in self.sequence:
            y = self.spiral_calculator.a174344(counter)
            x = self.spiral_calculator.a274923(counter)
            self.grid[i-x][j+y] = self.int_to_bool_function(a_n)
            counter += 1
