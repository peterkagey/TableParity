from b_file_parser import BFileParser
from b_file_lookup import BFileLookup
from boolean_list_to_file import BitmapWriter
from array_pattern import SpiralPattern, TablePattern
import os

class OeisToBmp:
    def __init__(self, sequence_name, pattern = TablePattern()):
        self.pattern = pattern
        self.sequence_name = sequence_name
        b_file = BFileLookup(sequence_name).b_file_txt()
        self.sequence = BFileParser(b_file).parsed_data

    def make_bmp(self):
        file_name = self.sequence_name + self.pattern.file_descriptor() + ".bmp"
        boolean_table = self.pattern.from_data(self.sequence)
        BitmapWriter(boolean_table).write_bitmap(file_name)
        os.system("open " + file_name)

table_sequences = ["A273620"] # read by antidiagonals
for sequence_name in table_sequences:
    print(sequence_name)
    OeisToBmp(sequence_name).make_bmp()

spiral_sequences = ["A280027"] # square spiral
for sequence_name in spiral_sequences:
    print(sequence_name)
    OeisToBmp(sequence_name, SpiralPattern()).make_bmp()
