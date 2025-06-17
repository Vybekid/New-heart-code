import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
            math.cos(2 * k) - 2 * \
            math.cos(3 * k) - \
            math.cos(4 * k)
x_scale_factor = 8.44  
y_scale_factor = 12    
bgcolor("black")
pencolor("#f73487")
speed(0)
for i in range(6000):
    x_coord = hearta(i) * x_scale_factor
    y_coord = heartb(i) * y_scale_factor
    goto(x_coord, y_coord)
    goto(0, 0)

done() 