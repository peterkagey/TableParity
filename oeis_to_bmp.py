from b_file_parser import BFileParser
from b_file_lookup import BFileLookup
from boolean_list_to_file import BitmapWriter
from spiral_array import SpiralArray
from table_array import TableArray
import os
import sympy
import math

class OeisToBmp:
    def __init__(self, sequence_name, list_to_array, int_to_bool_function = (lambda i: i & 1 != 0), file_descriptor = "_mod_2"):
        self.file_descriptor = file_descriptor
        self.int_to_bool_function = int_to_bool_function
        self.sequence_name = sequence_name
        b_file = BFileLookup(sequence_name).b_file_txt()
        self.sequence = BFileParser(b_file).parsed_data
        self.grid = list_to_array(self.sequence)

    def make_bmp(self):
        file_name = self.sequence_name + self.file_descriptor + "_spiral.bmp"
        BitmapWriter(self.grid).write_bitmap(file_name)
        os.system("open " + file_name)

list_of_sequences = ["A005150"]

def is_prime(n):
    if n > 1000000000:
        print(n)
        return False
    else:
        return sympy.isprime(n)

for sequence_name in list_of_sequences:
    print(sequence_name)
