import math
import numpy as np

# w_next = waypoints[closest_waypoints[1]]
# w_prev = waypoints[closest_waypoints[0]]

def dotproduct(w_next, w_prev, heading):
    """Dotproduct of the waypoint-vector and the cars unit vector
    
    Args:
        w_next (list): Coordinates of the Waypoint next in front of the car 
        w_prev (list): Coordinates of the Waypoint previous of the car 
        heading (float): The angle the car is heading in degree

    Returns:
        float: A value between -1 and 1 . If the car perfectely aims in the direction of the
        waypoint vector, it is 1. If it is perpendicular it is 0 and if it is in the opposite direction
        it is -1
    """
    w_waypoint = np.array(w_next) - np.array(w_prev)
    w_waypoint_u = w_waypoint / np.linalg.norm(w_waypoint)
    w_car = np.array([np.cos(heading * (np.pi/180)), np.sin(heading * (np.pi/180))])
    dotproduct = np.dot(w_waypoint_u, w_car)
    print(dotproduct)

    return dotproduct


def main():
    dotproduct(w_next=[2,3], w_prev=[3,2.7], heading=-30)

main()