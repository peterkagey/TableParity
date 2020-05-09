import math
from spiral_calculator import SpiralCalculator
from boolean_list_to_file import BitmapWriter
from plane_pattern import SpiralPattern
import os

#   21--22--23--24--25--26
#    |                   |
#   20   7---8---9---10  27
#    |   |           |   |
#   19   6   1---2  11  28
#    |   |       |   |   |
#   18   5---4---3  12  29
#    |               |   |
#   17--16--15--14--13  30
#                        |
#   36--35--34--33--32--31

class A334742:
    def __init__(self, n):
        self.sequence_length = n
        self.table_size = self.size_of_table()
        self.initialize_grid()
        self.fill_grid()
        self.sequence = self.unravel_grid()

    spiral_calculator = SpiralCalculator()

    def size_of_table(self):
        return math.ceil(math.sqrt(self.sequence_length))

    def center_of_table(self):
        n = self.size_of_table()
        if n % 2 == 0:
            return (n//2, n//2 - 1)
        else:
            return ((n-1)//2, (n-1)//2)

    def initialize_grid(self):
        self.center = self.center_of_table()
        self.grid = []
        for _ in range(self.table_size):
            self.grid.append([0] * self.table_size)

    def fill_grid(self):
        (i,j) = self.center
        self.grid[i][j] = 1
        for counter in range(2,self.sequence_length + 1):
            (x,y) = self.spiral_calculator.coordinate(counter)
            self.grid[i - y][j + x] = self.sum_all(x, y)

    def sum_north(self, x, y):
        if self.center[0] - y - 1 < 0:
            return 0
        sum = 0
        c = 1
        current_cell = self.grid[self.center[0] - y - c][self.center[1] + x]
        c += 1
        sum += current_cell
        return sum

    def in_bounds(self, x, y, x_d, y_d):
        x_value = self.center[1] + x + x_d
        if x_value < 0 or x_value >= self.table_size:
            return False
        y_value = self.center[0] - y - y_d
        return y_value >= 0 and y_value < self.table_size

    def sum_direction(self, x, y, x_d, y_d):
        if self.in_bounds(x, y, x_d, y_d):
            return self.grid[self.center[0] - y - y_d][self.center[1] + x + x_d]
        return 0

    def sum_all(self, x, y):
        sums = 0
        for x_d, y_d in [(0,1),(1,0),(-1,0),(0,-1)]:
            sums += self.sum_direction(x,y,x_d,y_d)
        return sums

    def unravel_grid(self):
        (i,j) = self.center
        sequence = []
        self.grid[i][j] = 1
        for counter in range(1,self.sequence_length + 1):
            (x,y) = self.spiral_calculator.coordinate(counter)
            sequence.append((counter, self.grid[i - y][j + x]))
        return sequence

# print(list(map(lambda x: x[1], A334742(400).grid)))
# print(A334742(400).grid)

file_name = "rook_spiral_test.bmp"
boolean_table = SpiralPattern().from_data(A334742(400).sequence)
BitmapWriter(boolean_table).write_bitmap(file_name)
os.system("open " + file_name)

