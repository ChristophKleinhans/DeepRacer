import math

import matplotlib.pyplot as plt
import numpy as np
#from shapely import Point, LineString
from shapely.geometry import LineString, Point


raceline = [[2.90999528, 0.68319247],
            [3.73488764, 0.68851628],
            [3.73488764, 0.68851628],
            [3.73488764, 0.68851628],
            [4.0669553 , 0.6836061 ],
            [4.69045564, 0.68382901],
            [5.32000213, 0.68405407],
            [5.42921276, 0.68469042],
            [5.76139454, 0.70141596],
            [6.05061299, 0.7524216 ],
            [6.28589663, 0.83358135],
            [6.4763073 , 0.94176249],
            [6.62840817, 1.07415805],
            [6.74359597, 1.22865132],
            [6.8202571 , 1.40241976],
            [6.85533639, 1.59099579],
            [6.84461341, 1.78792063],
            [6.78548351, 1.98424031],
            [6.67846624, 2.17006883],
            [6.52694366, 2.3369323 ],
            [6.33602803, 2.47953013],
            [6.11146298, 2.59642914],
            [5.85926127, 2.68977726],
            [5.58676609, 2.76510056],
            [5.29507044, 2.85870704],
            [5.01492854, 2.96554663],
            [4.748076  , 3.0864171 ],
            [4.49616752, 3.22144359],
            [4.26069968, 3.36990618],
            [4.04373102, 3.53053496],
            [3.8478699 , 3.70037287],
            [3.68532422, 3.86444291],
            [3.52475633, 4.00413156],
            [3.36197364, 4.1235435 ],
            [3.19524957, 4.22347828],
            [3.0222006 , 4.30397303],
            [2.83977023, 4.36381049],
            [2.64494882, 4.4002502 ],
            [2.43604956, 4.40877315],
            [2.21426434, 4.38355161],
            [1.98465684, 4.31872003],
            [1.75572568, 4.21005765],
            [1.53787954, 4.05526597],
            [1.34133998, 3.85555506],
            [1.17537578, 3.61399834],
            [1.04877126, 3.33533118],
            [0.97025504, 3.02776724],
            [0.94633919, 2.70880642],
            [0.97398134, 2.41033639],
            [1.03869235, 2.15202912],
            [1.13454111, 1.91798756],
            [1.2613579 , 1.70025633],
            [1.42015414, 1.49800443],
            [1.6113874 , 1.31331395],
            [1.83425854, 1.14935648],
            # [2.08546371, 1.00964885],
            # [2.35746331, 0.89722922],
            # [2.6382989 , 0.81375861],
            [2.90999528, 0.68319247]]

def offset_func(translation):
    return (-3 * translation + 1)

def raceline_reward(raceline, agent_x, agent_y, agent_heading):
    """_summary_

    Args:
        raceline (_type_): The perfect raceline
        agent_x (_type_): x-position by the agent
        agent_y (_type_): y-position by the agent
        heading (_type_): heading in degree of the agent

    Returns:
        _type_: _description_
    """
    
    # Parameters
    agent_location = Point(agent_x, agent_y)
    raceline = LineString(raceline)

    plt.plot(raceline.xy[0], raceline.xy[1])
    plt.scatter(agent_location.xy[0], agent_location.xy[1])

    

    # Calculate a reward when the agent has translation to the perfect raceline
    translation = agent_location.distance(raceline)    
    reward_translation = offset_func(translation)

    if reward_translation > 0:
        pass
    else:
        reward_translation = 0

    # Calculate the reward how the agent is heading
    shift = 0.16    
    point_on_raceline = raceline.interpolate(raceline.project(agent_location))
    point_on_raceline_shifted = raceline.interpolate(raceline.project(agent_location)+shift)

    plt.scatter(point_on_raceline.xy[0], point_on_raceline.xy[1])
    plt.scatter(point_on_raceline_shifted.xy[0], point_on_raceline_shifted.xy[1])
    

    raceline_heading = np.array([point_on_raceline_shifted.xy[0], point_on_raceline_shifted.xy[1]]) - np.array([point_on_raceline.xy[0], point_on_raceline.xy[1]])

    # Dotproduct
    raceline_heading_norm = raceline_heading / np.linalg.norm(raceline_heading)
    agent_heading = np.array([[np.cos(agent_heading * (np.pi/180))], [np.sin(agent_heading * (np.pi/180))]])
    agent_heading_norm = agent_heading / np.linalg.norm(agent_heading)
    dotproduct = np.dot(np.transpose(raceline_heading_norm), agent_heading_norm)

    if dotproduct > 0:
        reward_dotproduct = dotproduct[0][0]
    else:
        reward_dotproduct = 0

    print("Reward translation: ", reward_translation, "Reward dotproduct", reward_dotproduct)
    
    #return (reward_translation, reward_dotproduct)
    
    
    
    plt.scatter(point_on_raceline_shifted.xy[0], point_on_raceline_shifted.xy[1]) # point on raceline_shifted
    plt.plot([point_on_raceline.xy[0][0], point_on_raceline_shifted.xy[0][0]], [point_on_raceline.xy[1][0], point_on_raceline_shifted.xy[1][0]])
    plt.plot([0, raceline_heading[0][0]], [0, raceline_heading[1][0]]) # raceline heawding
    plt.plot([0, agent_heading[0][0]], [0, agent_heading[1][0]])

    plt.show()



print(raceline_reward(raceline, 5.44, 2.76, 0))


def raceline_min_radius(raceline):
    raceline = LineString(raceline)
    #min_radius = minimum_bounding_radius(raceline)
    print(min_radius)

    wheelbase = 0.15
    max_curve_radius = 0.5842 - wheelbase
    max_steering_angle = math.atan(wheelbase/max_curve_radius)
    maximum_steering_angle_degree = max_steering_angle * (180/math.pi)

#raceline_min_radius(raceline=raceline)