import math
import numpy as np
# Clase que incluye funciones usadas en tiro parabólico
class Parabola:
    # Constructor
    def __init__(self, g=9.81, vo=0, alpha=0):
        self.g = g
        self.vo = vo
        self.alpha = alpha*math.pi/180
        self.R = 0
        self.tv = 0
        self.ym = 0
    # Asigna valor de gravedad
    def set_g(self, g):
        self.g = g
    # Asigna el valor de la rapidez inicial
    def set_vo(self, vo):
        self.vo = vo
    # Asigna el valor del ángulo de disparo
    def set_alpha(self, alpha):
        self.alpha = alpha
    # Cálculo del tiempo de vuelo
    def tiempo_vuelo(self):
        self.tv = 2*self.vo*math.sin(self.alpha)/self.g
        return self.tv
    # Alcance
    def alcance(self):
        self.R = (self.vo**2)*math.sin(2*self.alpha)/self.g
        return self.R
    # Altura máxima
    def altura_maxima(self):
        self.ym = 0.5*(self.vo**2)*(math.sin(self.alpha)**2)/self.g
        return self.ym
    # Trayectoria
    def trayectoria(self):
        t = np.linspace(0, self.tiempo_vuelo(),1000)
        x = self.vo*math.cos(self.alpha)*t
        y = self.vo*math.sin(self.alpha)*t - 0.5*self.g*(t**2)
        return x, y