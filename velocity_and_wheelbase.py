import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def v_max_func(steering_angle_in_deg):
    g = 9.81
    mü_r = 0.9
    w_fw = 0.15
    theta = abs(steering_angle_in_deg) * (math.pi / 180) # only positive values
    return steering_angle_in_deg, math.sqrt(g * mü_r * w_fw * 1/(math.tan(theta + 0.0717516)))

def centrifugal_limit_reward(speed, steering_angle, v_max_func):
    """The maximal speed in dependence of the steering angle before losing grip
        The more the car is at the limit, the more reward it is getting
        v = sqrt(g*mü_r*w_fw*(1/tan(theta)))
        g = gravital acceleration
        mü_r = the tranction coefficient
        w_fw = the distance between the two front wheels in meter
        theta = the steering angle
    Args:
        speed (floag): of the car in m/s
        steering_angle (float): of the front wheels in degree
    """

    v_max = v_max_func(steering_angle_in_deg=steering_angle)[1]
    
    # rewarding when he get to the maximum possible speed for that angle
    if speed > v_max:
        reward = 1e-3
    else:
        reward = speed / v_max

    return reward

def maximum_steering_angle():
    """Calculates which max steering angle is needed
    """
    wheelbase = 0.15
    max_curve_radius = 0.5842 - wheelbase
    max_steering_angle = math.atan(wheelbase/max_curve_radius)
    maximum_steering_angle_degree = max_steering_angle * (180/math.pi)

    print(maximum_steering_angle_degree)


def linear_vmax_func(speed, steering_angle_in_deg):
    theta = abs(steering_angle_in_deg)
    v_max = (-0.1 * theta) + 4
    print("VMAX: ", v_max)
    if speed > v_max:
        reward = 1e-3
    else:
        reward = speed / v_max

    return reward


# angle_list = []
# speed_list = []
# for angle in range(0,31,1):
#     print("The angle is {} and the max speed is {}".format(v_max_func(angle)[0], v_max_func(angle)[1]))
#     angle_list.append(float(v_max_func(angle)[0]))
#     speed_list.append(float(v_max_func(angle)[1]))


print(linear_vmax_func(10,3))

# plt.scatter(angle_list, speed_list)
# plt.show()


#centrifugal_limit_reward(speed=2.3, steering_angle=-8, v_max_func=v_max_func)




