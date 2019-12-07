from scipy import special
from sympy.abc import x, y
import math

def comb(n,k) : return special.comb(n,k, exact = True)

x = int(input("Enter the Coefficent,c, of X: ")) * x

e = int(input("Enter the value of the constant m : "))

p = int(input("Enter the power you want to raise (cx+m) to : "))

pt = []

for i in range(0,p+1): pt.append(comb(p,i))

for i in range(0,p+1):
    print (pt[i]*(x**i)*(e**(p-i)))
