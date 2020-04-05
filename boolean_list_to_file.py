from functools import reduce

class BitmapWriter:

    def __init__(self, list_of_boolean_lists):
        self.list_of_boolean_lists = list_of_boolean_lists
    
    # This expects a list of exactly eight bools, but it doesn't check.
    def to_byte(self, boolean_list):
        s = 0
        for b in boolean_list:
            s <<= 1
            if b: s ^= 1
        return s

    def to_padded_byte_array(self, boolean_list):
        pad_length = -len(boolean_list) % 32
        padded_array = boolean_list + [False] * pad_length
        return bytes([self.to_byte(padded_array[8*i:8*i+8]) for i in range(len(padded_array)//8)])

    def little_endian(self, value, byte_count):
        return bytes([(value >> 8*i) & 0xFF for i in range(byte_count)])

    # 14 bytes
    def bmp_file_header(self, width, height):
        header_field     = bytes([0x42, 0x4D])
        padded_width     = width + (-width % 32)
        file_size        = self.little_endian(14 + 40 + 8 + (padded_width * height) // 8, 4)
        reserved         = self.little_endian(0, 4)
        starting_address = self.little_endian(14 + 40 + 8, 4)
        return header_field + file_size + reserved + starting_address

    # BITMAPINFOHEADER
    def dib_header(self, width, height):
        size_of_header        = self.little_endian(40, 4) # 40 bytes
        pixel_width           = self.little_endian(width, 4)
        pixel_height          = self.little_endian(height, 4)
        color_planes          = self.little_endian(1, 2)
        bits_per_pixel        = self.little_endian(1, 2)
        compression_method    = self.little_endian(0, 4) # BI_RGB (uncompressed)
        image_size            = self.little_endian(0, 4) # a dummy 0 can be given for BI_RGB bitmaps.
        horizontal_resolution = self.little_endian(255, 4)
        vertical_resolution   = self.little_endian(255, 4)
        number_of_colors      = self.little_endian(2, 4) # 0 to default to 2n
        important_colors      = self.little_endian(0, 4) # 0 when every color is important
        return size_of_header + pixel_width + pixel_height + color_planes + bits_per_pixel + compression_method + image_size + horizontal_resolution + vertical_resolution + number_of_colors + important_colors

    def color_table(self):
        white = self.little_endian(0xffffffff, 4)
        black = self.little_endian(0x00000000, 4)
        return black + white

    def pixel_data(self):
        list_of_byte_arrays = map(self.to_padded_byte_array, self.list_of_boolean_lists)
        return reduce(lambda b1, b2: b2 + b1, list_of_byte_arrays)

    def bmp(self):
        height = len(self.list_of_boolean_lists)
        width  = len(self.list_of_boolean_lists[0])
        return self.bmp_file_header(width, height) + self.dib_header(width, height) + self.color_table() + self.pixel_data()

    def write_bitmap(self, file_name):
        with open(file_name, 'wb') as output:
            output.write(self.bmp())
