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

class SpiralSequence:
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
            self.grid[i - y][j + x] = self.cell_value(x, y)

    def cell_value(self, x, y):
        raise NotImplementedError

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

    def unravel_grid(self):
        (i,j) = self.center
        sequence = []
        for counter in range(1,self.sequence_length + 1):
            (x,y) = self.spiral_calculator.coordinate(counter)
            sequence.append((counter, self.grid[i - y][j + x]))
        return sequence

class A334742(SpiralSequence):
    def cell_value(self, x, y):
        sums = 0
        for x_d, y_d in [(0,1),(1,0),(-1,0),(0,-1)]:
            sums += self.sum_direction(x,y,x_d,y_d)
        return sums

class A334745(SpiralSequence):
    def cell_value(self, x, y):
        sums = 0
        for x_d, y_d in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            sums += self.sum_direction(x,y,x_d,y_d)
        return sums

class A334746(SpiralSequence):
    def cell_value(self, x, y):
        sums = 0
        for x_d, y_d in [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            sums += self.sum_direction(x,y,x_d,y_d)
        return sums

class A334741(SpiralSequence):
    def cell_value(self, x, y):
        sums = 0
        for x_d, y_d in [(0,1),(1,0),(-1,0),(0,-1)]:
            sums += self.sum_line(x,y,x_d,y_d)
        return sums

    def sum_line(self, x, y, x_d, y_d):
        sums = 0
        c = 1
        while self.in_bounds(x, y, c*x_d, c*y_d):
            sums += self.grid[self.center[0] - y - c*y_d][self.center[1] + x + c*x_d]
            c += 1
        return sums

class PascalsSpiral(SpiralSequence):
    def cell_value(self, x, y):
        sums = 0
        for a, b in self.coordinates_leftbehind(x, y):
            sums += self.grid[self.center[0] - b][self.center[1] + a]
        return sums

    def coordinates_leftbehind(self, x, y):
        if y == 1 - x and x > 0: # bottom right corner
            return [(x-1, y)]
        if y == x and x > 0:     # top right corner
            return [(x, y - 1)]
        if y == -x and x < 0:    # top left corner
            return [(x + 1, y)]
        if y == x and x < 0:     # bottom left corner
            return [(x, y + 1)]
        if x > y and x > 1 - y:  # right section
            return [(x, y - 1), (x - 1, y)]
        if y > abs(x):           # top section
            return [(x + 1, y), (x, y - 1)]
        if x < -abs(y):          # left section
            return [(x, y + 1), (x + 1, y)]
        if y < x and y < 1 - x:  # underbelly
            return [(x - 1, y), (x, y + 1)]
        raise IndexError


# print(list(map(lambda x: x[1], A334742(100).sequence)))
# print(PascalsSpiral(25).sequence)

file_name = "PascalsSpiral_test.bmp"
boolean_table = SpiralPattern().from_data(PascalsSpiral(10000).sequence)
BitmapWriter(boolean_table).write_bitmap(file_name)
os.system("open " + file_name)
