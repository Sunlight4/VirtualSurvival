from __future__ import division
import math
class Vector(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    def normalize(self):
        newx=self.x/self.magnitude()
        newy=self.y/self.magnitude()
        return Vector(newx, newy)
    def direction(self):
        return math.atan(self.y/self.x)
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)
    def __div__(self, other):
        return Vector(self.x/other, self.y/other)
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def __cmp__(self, other):
        return cmp(self.magnitude(), other.magnitude())
def dot(vector1, vector2):
    return vector1.x*vector2.x+vector1.y*vector2.y
def angle(vector1, vector2):
    norm1=vector1.normalize()
    norm2=vector2.normalize()
    return math.acos(dot(norm1, norm2))

