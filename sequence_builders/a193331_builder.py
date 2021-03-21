from boolean_list_to_file import BitmapWriter

def primes_up_to(n):
    upper_bound = n + 1
    number_list = [True] * upper_bound
    number_list[0] = False
    number_list[1] = False

    current_prime = 2
    while current_prime**2 < upper_bound:
        for n in range(current_prime**2, upper_bound, current_prime):
            number_list[n] = False
        current_prime += number_list[current_prime + 1:len(number_list)].index(True) + 1

    primes_list = []
    for i in range(2, upper_bound):
        if number_list[i]:
            primes_list.append(i)

    return primes_list

class A193331Builder:
    def __init__(self, size):
        self.size = size
        self.grid = [[False] * size for _ in range(size)]
        self.primes = primes_up_to(200000)
        self.fill_grid()

    def fill_grid(self):
        for n in range(1,2*self.size):
            k_min = max(1, n - self.size + 1)
            k_max = min(n+1, self.size + 1)
            for k in range(k_min,k_max):
                if (((k-1)*n**2)//(2*k)) & 1 == 1:
                    self.grid[n-k][k-1] = True

BitmapWriter(A193331Builder(500).grid).write_bitmap("A193331_500.bmp")
