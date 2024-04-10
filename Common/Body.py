from vector2D import *
import c4dynamics as c4d
#parent class
class Body:
    #region contructors
    def __init__(self, initial_pos, initial_vel, mass):
        self.__initial_pos = initial_pos
        self.__initial_vel = initial_vel
        self.mass = mass

        self._X0 = [self.initial_pos.x, self.initial_pos.y, self.initial_vel.x, self.initial_vel.y]

    #endregion

    #region getters and setters
    
    @property
    def initial_pos(self):
        return self.__initial_pos
    
    @initial_pos.setter
    def initial_pos(self, initial_pos):
        self.__initial_pos = initial_pos

    @property
    def initial_vel(self):
        return self.__initial_vel
    
    @initial_vel.setter
    def initial_vel(self, initial_vel):
        self.__initial_vel = initial_vel

    #endregion

#region Child class of body for planets(TO-DO)
class Planet(Body):
    #AU variable goes here
    #region Constructors
    def __init__(self, initial_pos, initial_vel, mass, color, radius):
        super().__init__(initial_pos, initial_vel, mass)
        self.__radius = radius
        self.__color = color
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        #self.x
        #self.y
        #self.x_vel
        #self.y_vel
    
    #endregion

    #region getters and setters
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
    #endregion

#class for object in projectile motion(TO-DO)
class RegularBody(Body):
    #region constructors
    def __init__(self, initial_pos, initial_vel, mass, radius):
        super().__init__(initial_pos, initial_vel, mass)
        self.__radius = radius

        self._pt = c4d.datapoint(x = self._X0[0], y = self._X0[1], vx = self._X0[2], vy = self._X0[3])
        self._pt.mass = mass

    #endregion

    #region getters and setters
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    #endregion

#Class for generic body with point mass      
class Particle(Body):
    #region global properties
    n = 0
    #endregion
    #region Constructors
    def __init__(self, initial_pos, initial_vel, mass):
        super().__init__(initial_pos, initial_vel, mass)
        self.i = Particle.n
        Particle.n += 1
        self._pt = c4d.datapoint(x = self._X0[0], y = self._X0[1], vx = self._X0[2], vy = self._X0[3])
        self._pt.mass = mass

    #endregion
