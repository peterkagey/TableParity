from b_file_parser import BFileParser
from b_file_lookup import BFileLookup
from boolean_list_to_file import BitmapWriter
import os

class OeisToBmp:
    def __init__(self, sequence_name):
        self.sequence_name = sequence_name
        b_file = BFileLookup(sequence_name).b_file_txt()
        self.sequence = BFileParser(b_file).parsed_data
        self.initialize_boolean_grid()
        self.fill_boolean_grid()

    def make_bmp(self):
        BitmapWriter(self.grid).write_bitmap(self.sequence_name + ".bmp")
        os.system("open " + self.sequence_name + ".bmp")
    
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
        for (n,a_n) in self.sequence:
            self.grid[i][j] = (a_n % 2 == 1)
            if i == 0:
                i = j + 1
                j = 0
            else:
                i -= 1
                j += 1

list_of_sequences = ["A282814", "A275257", "A282812", "A304027", "A330541", "A271709", "A271710", "A273620", "A279965", "A279968", "A284486", "A285521", "A301851", "A301853", "A328071", "A268040", "A268978", "A276162", "A327844", "A330590", "A269526", "A083140", "A268057", "A279966", "A279967", "A107435", "A185869", "A271439", "A280172", "A282813", "A279211"]

for sequence_name in list_of_sequences:
    OeisToBmp(sequence_name).make_bmp()

