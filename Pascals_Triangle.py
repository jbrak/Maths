from scipy import special

def comb(n,k) : return special.comb(n,k, exact = True)

value = int(input('Enter the Value to Draw Pascals Triangle to: '))


for i in range(0,value):
    pt = []
    for x in range(0,i+1): pt.append(comb(i,x))
    print(pt)
