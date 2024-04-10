import numpy as np
import sympy as sp
class Vect2:
    #region Contructors
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #endregion
    
    #region getters and setters
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

    #endregion
        
    #region Methods
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, v):
        return Vect2(self.x + v.x, self.y + v.y)
    
    def __radd__(self, v):
        return Vect2(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return Vect2(self.x - v.x, self.y - v.y)
    
    def __rsub__(self, v):
        return Vect2(v.x - self.x, v.y - self.y)
    
    def __mul__(self, n):
        return Vect2(self.x * n, self.y * n)
    
    def __rmul__(self, n):
        return Vect2(self.x * n, self.y * n)
    
    def dot(self, v):
        return self.x * v.x + self.y * v.y
    
    def get_length(self):
        return np.sqrt(self.dot(self))
    
    #endregion
