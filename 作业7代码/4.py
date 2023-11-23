
import math

class Vector:
    def __init__(self, components):
        self.components = components

    def check_length(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same length")

    def add(self, other):
        self.check_length(other)
        return Vector([x + y for x, y in zip(self.components, other.components)])

    def subtract(self, other):
        self.check_length(other)
        return Vector([x - y for x, y in zip(self.components, other.components)])

    def dot(self, other):
        self.check_length(other)
        return sum(x * y for x, y in zip(self.components, other.components))

    def norm(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def __str__(self):
        return f'({",".join(map(str, self.components))})'

    def equals(self, other):
        return self.components == other.components



