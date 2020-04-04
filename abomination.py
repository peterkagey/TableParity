from random import randrange

# This expects a list of exactly eight bools, but it doesn't check.
def to_byte(boolean_list):
    s = 0
    for b in boolean_list:
        s <<= 1
        if b: s ^= 1
    return s

# This expects the list to be a multiple of 8.
def to_byte_array(boolean_list):
    return bytes([to_byte(boolean_list[8*i:8*i+8]) for i in range(len(boolean_list)//8)])

def little_endian(value, byte_count):
    return bytes([(value >> 8*i) & 0xFF for i in range(byte_count)])

def random_data(byte_count):
    data = []
    for _ in range(byte_count):
        data.append(randrange(256))
    return bytes(data)

# 14 bytes
def bmp_file_header(width, height):
    header_field     = bytes([0x42, 0x4D])
    file_size        = little_endian(14 + 40 + 8 + (width * height) // 8, 4)
    reserved         = little_endian(0, 4)
    starting_address = little_endian(14 + 40 + 8, 4)
    return header_field + file_size + reserved + starting_address

# BITMAPINFOHEADER
def dib_header(width, height):
    size_of_header        = little_endian(40, 4) # 40 bytes
    pixel_width           = little_endian(width, 4)
    pixel_height          = little_endian(height, 4)
    color_planes          = little_endian(1, 2)
    bits_per_pixel        = little_endian(1, 2)
    compression_method    = little_endian(0, 4) # BI_RGB (uncompressed)
    image_size            = little_endian(0, 4) # a dummy 0 can be given for BI_RGB bitmaps.
    horizontal_resolution = little_endian(255, 4)
    vertical_resolution   = little_endian(255, 4)
    number_of_colors      = little_endian(2, 4) # 0 to default to 2n
    important_colors      = little_endian(0, 4) # 0 when every color is important
    return size_of_header + pixel_width + pixel_height + color_planes + bits_per_pixel + compression_method + image_size + horizontal_resolution + vertical_resolution + number_of_colors + important_colors

def color_table():
    white = little_endian(0xffffffff, 4)
    black = little_endian(0x00000000, 4)
    return black + white

def random_bmp(width, height):
    return bmp_file_header(width, height) + dib_header(width, height) + color_table() + random_data((width * height)//8)

def flatten(l):
    return [item for sublist in l for item in sublist]


def bmp(list_of_boolean_lists):
    height = len(list_of_boolean_lists)
    width  = len(list_of_boolean_lists[0])
    bitMap = to_byte_array(flatten(list_of_boolean_lists))
    # print(height)
    # print(width)
    # print(flatten(list_of_boolean_lists))
    return bmp_file_header(width, height) + dib_header(width, height) + color_table() + bitMap

n = 2**12
grid = []
for i in range(4*n):
    grid.append([False] * n)
grid[0][0] = True
grid[1][0] = True
grid[0][1] = False

column_parity = [False] * n
row_parity = [False] * (4*n)
row_parity[0] = True
row_parity[1] = True
top_diagonal_parity = [False] * (4*n)
diagonal_parity = [False] * (4*n)
diagonal_parity[0] = True
diagonal_parity[1] = True
antidiagonal_parity = False

for i in range(2,4*n): 
    antidiagonal_parity = False
    for j in range(i+1):
        if j >= n:
            break
        if i-j >= j:
            # calculate sum
            grid[i-j][j] = column_parity[j] ^ row_parity[i-j] ^ antidiagonal_parity ^ diagonal_parity[i - 2*j]
            # adjust the helper sums
            antidiagonal_parity = (antidiagonal_parity ^ grid[i-j][j])
            diagonal_parity[i-2*j] = (diagonal_parity[i-2*j] ^ grid[i-j][j])
            column_parity[j] = (column_parity[j] ^ grid[i-j][j])
            row_parity[i-j] = (row_parity[i-j] ^ grid[i-j][j])
        else:
            # calculate sum
            grid[i-j][j] = column_parity[j] ^ row_parity[i-j] ^ antidiagonal_parity ^ top_diagonal_parity[2*j-i]
            # adjust the helper sums
            antidiagonal_parity = (antidiagonal_parity ^ grid[i-j][j])
            top_diagonal_parity[2*j-i] = (top_diagonal_parity[2*j-i] ^ grid[i-j][j])
            column_parity[j] = (column_parity[j] ^ grid[i-j][j])
            row_parity[i-j] = (row_parity[i-j] ^ grid[i-j][j])

# print(grid)

with open("example.bmp", 'wb') as output:
    output.write(bmp(grid[0:2*n]))