
from math import atan
from cmath import polar

def conversor(coord_cart_x, coord_cart_y):
    coord_polar_r = (coord_cart_x**2 + coord_cart_y**2)**0.5
    coord_polar_theta = atan(coord_cart_y/coord_cart_x)
    return coord_polar_r, coord_polar_theta

coord_cart_x= float(input("informe o valor da coordenada cartesiana x: "))
coord_cart_y= float(input("informe o valor da coordenada cartesiana y: "))

print(polar(complex(coord_cart_x,coord_cart_y)))
coord_polar=(conversor(coord_cart_x,coord_cart_y))
print(coord_polar)
