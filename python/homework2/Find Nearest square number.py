import math

def nearest_sq(n):
    sqrt_n = math.isqrt(n) 
    lower_square = sqrt_n ** 2
    upper_square = (sqrt_n + 1) ** 2

    if abs(n - lower_square) <= abs(n - upper_square):
        return lower_square
    else:
        return upper_square