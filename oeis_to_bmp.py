from b_file_parser import BFileParser
from b_file_lookup import BFileLookup
from boolean_list_to_file import BitmapWriter
from plane_pattern import SpiralPattern, TablePattern
import os
import time

class OeisToBmp:
    def __init__(self, sequence_name, pattern = TablePattern()):
        self.pattern = pattern
        self.sequence_name = sequence_name
        b_file = BFileLookup(sequence_name).b_file_txt()
        self.sequence = BFileParser(b_file).parsed_data

    def make_bmp(self):
        file_name = "images/bulk_lookup/" + self.sequence_name + self.pattern.file_descriptor() + ".bmp"
        boolean_table = self.pattern.from_data(self.sequence)
        BitmapWriter(boolean_table).write_bitmap(file_name)
        os.system("open " + file_name)

table_sequences = sorted(['A122848', 'A163936', 'A168561']) # from search_scraper.py
for sequence_name in table_sequences:
    print(sequence_name, table_sequences.index(sequence_name)+1, "of", len(table_sequences))
    OeisToBmp(sequence_name).make_bmp()
    time.sleep(4) # Throttle requests so that the OEIS servers aren't hit too hard.
