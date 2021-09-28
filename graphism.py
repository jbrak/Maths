from scipy import special
from sympy import symbols
import math
from plotnine import *

yzz = []

for i in range(0,8):
    y = (i**2) + 2
    yzz.append(y)

print(yzz)
