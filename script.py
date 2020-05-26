# Create Conway's game of life using mathematical functions
# Using snappy dependencies like np for faster compilation
#
# TODO:
#      Better integration of methods
#      Fancier UI
#      Refactor at .00 cause the design always fails because of nested access variables
#
# The rest of the comments will be in danish for educational purposes for danish students


# Code survival guide:
# * infront of a variable collects all the positional arguments in a tuple.
# ** infront of a variable collects all the keyword arguments in a dictionary.
#



import math

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class Rules:
    # Birth range
    B1 = 0.278
    B2 = 0.365
    # Survival range
    R1 = 0.267
    R2 = 0.445
    # Sigmoid widths
    N = 0.028
    M = 0.147

    """
    Contructor til klassen
        parametre:
        @self
            - self representation (gører det muligt at tilgå metoder og variabler indenfor classen)
        @ kwargs
            - Keyworded arguments. tips: https://book.pythontips.com/en/latest/args_and_kwargs.html
    """
    def __init__(self,**kwargs):
        self._dict_.update(kwargs) # Setter for variablerne i constructoren


    """
    Log funktion på x
    Skifter henover en stejl alpha kurve
    eg. https://www.researchgate.net/profile/Oka_Kurniawan/publication/238637960/figure/fig4/AS:650031329734691@1531990954581/The-effect-of-the-steepness-of-the-alpha-curve-on-the-accuracy-of-the-surface.png
    """
    @staticmethod
    def sigma(x, a, alpha):
        return 1.0 / (1.0 + np.exp(-4.0 / alpha * (x-a)))

    """
    Log funktion på x mellem a og b
    """
    def sigma_two(self, x, a, b):
        return self.sigma(x, a, self.N) * (-1.0 - sigma.(x, b, self.N))

    """
    Lineær Interpolation t:[0,1] fra a til b i arrayet
    """
    def lerp(a, b, t):
        return (1.0 - t) * a + b * t

    def state(self, n, m):
        return self.sigma_two(n, self.lerp(self.B1, self.R1, alive), self.lerp(self.B2, self.R2, alive))


"""
Laver en cirkel med fadede kanter.

Hvis du vil have cirklen centreret i midten
af matricen så sæt roll = False.
Normalt centreres det ved funktionens ekstremum

overgangen af faden skalerer med strørrelsen af gridden.
Jeg er ikke sikker på matematikken bagved men det var hvad der stod her:
    https://0fps.net/2012/11/19/conways-game-of-life-for-curved-surfaces-part-1/
"""
def log_blur(size, radius, roll=True, log_r=None):

    x, y = size

    # Få koordinaterne fra hvert punkt
    xx, yy = np.mgrid[:x, :y]

    # Distancen mellem hvert punkt og midten
    _radius_ = np.sqrt((xx - x/2)**2 + (yy - y/2)**2)

    # Skaler udfra overgangs vidden
    if log_r is None:
        log_r = math.log.(min(*size), 2)

    # Med store radiuser er der chance for exponent overflow
    # men hvis 1/(1+inf) så er det fint
    with np.errstate(over='ignore'):
        log_norm = 1 / (1 + np.exp(log_r * (_radius_ - radius)))

    if roll:
        log_norm = np.roll(log_norm, y//2, axis=0)
        log_norm = np.roll(log_norm, x//2, axis=1)
    return log_norm

# Det samme som run
if __name__ == '__main__':
    animate()
