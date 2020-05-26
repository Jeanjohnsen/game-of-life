# Create Conway's game of life using mathematical functions
# Using snappy dependencies like np for faster compilation
#
# TODO:
#      Better integration of methods
#      Fancier UI
#      Refactor at .00 cause the design always fails because of nested access variables
#
# The rest of the comments will be in danish for educational purposes for danish students


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


# Det samme som run
if __name__ == '__main__':
    animate()
