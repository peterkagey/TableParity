import math

class SpiralCalculator:
    def a000196(self, n):
        return int(math.sqrt(n))

    def a001057(self,n):
        return (n + 1)//2 * (-1)**(n+1)

    def a002522(self,n):
        return n**2 + 1

    def a002061(self,n):
        return n**2 - n + 1

    def a003059(self,n):
        return math.ceil(math.sqrt(n))

    def a174344(self,n):
        k = self.a000196(n-1)
        j = n - self.a002061(k+1)
        if n == 1:
            return 0
        elif self.a002522(k) <= n and n <= self.a002061(k+1):
            return self.a001057(k)
        elif k % 2 == 1:
            return self.a001057(k) - j
        else:
            return self.a001057(k) + j

    def a274923(self,n):
        k = self.a003059(n-1)
        j = n - self.a002522(k-1)
        if n == 1:
            return 0
        elif self.a002061(k) <= n and n <= self.a002522(k+1):
            return self.a001057(k-1)
        elif k % 2 == 1:
            return self.a001057(k-2) - j
        else:
            return self.a001057(k-2) + j
