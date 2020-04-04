from b_file_lookup import BFileLookup 

class BFileParser:
    def __init__(self, b_file_text):
        self.b_file_text = b_file_text
        self.parsed_data = self.parse()

    def parse_data_string(self, data_string):
        i, a_i = data_string.split(" ")
        return (int(i), int(a_i))

    def parse(self):
        b_file_lines = map(lambda s: s.strip(),self.b_file_text.splitlines())
        b_file_data = filter(self.is_data_line, b_file_lines)
        return list(map(self.parse_data_string, b_file_data))

    def is_data_line(self, b_file_line):
        return (len(b_file_line) > 0) and (b_file_line[0] != '#')

print(BFileParser(BFileLookup("A279212").b_file_txt()).parsed_data) 