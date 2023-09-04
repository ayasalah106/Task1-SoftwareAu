import math
class ComplexNumber:
    """     A class representing a complex number.
    ComplexNumber objects can be used to perform arithmetic operations 
    Args:
        real (float): The real part of the complex number.
        imaginary (float): The imaginary part of the complex number.  """
    def __init__(self, real, imag):
        self.real = real
        self.imag= imag
    def __add__(self, other):
        return ComplexNumber(self.real + other.real,  self.imag + other.imag)
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        prod_real = (self.real * other.real) - (self.imag * other.imag)
        prod_imag = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(prod_real, prod_imag)
    def __truediv__(self, other):
        denominator = (other.real ** 2) + (other.imag ** 2)
        real_quot = ((self.real * other.real) + (self.imag * other.imag)) / denominator
        imag_quot = ((self.imag * other.real) - (self.real * other.imag)) / denominator
        return ComplexNumber(real_quot, imag_quot)
    def mod(self):
        return f"{math.sqrt((self.real**2)+ (self.imag ** 2)):0.2f}"
    #fun to print in this format
    def __str__(self):
        return f"{self.real:0.2f}{'+' if self.imag >= 0 else '-'}{abs(self.imag):0.2f}i"
C = ComplexNumber(3, 2)
D = ComplexNumber(-4, -5)
# Output
print("C + D =",C+D)
print("C - D =",C-D)
print("C * D =", C*D)
print("C / D =", C/D)
print("mod(C) =", C.mod())
print("mod(D) =", D.mod())
