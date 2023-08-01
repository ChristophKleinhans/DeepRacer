import math
import seaborn as sns

"""
track_width = the width of the track - re:invent 2018 = 0.76m 
d_c = distance from the center
w_wheels = the width of the wheels
d_c_outer_wheel = distance of the outer wheel from the center -> d_c + 0.5 * w_wheels

"""

def d_c_outer_wheel(d_c, w_wheels):
    return (d_c + 1/2 * w_wheels)


def xsquared(d_center, width_wheels):
    outer_wheel = d_center + 1/2 * width_wheels
    return (1 - (outer_wheel**2 )**(1/12) * 0.75)
    # return(1 - x^3)



d_c_outer_wheel = d_c_outer_wheel(d_c=0.25, w_wheels=0.15)
print("The distance of the outer wheel ", d_c_outer_wheel)

print(xsquared(d_c_outer_wheel=d_c_outer_wheel))