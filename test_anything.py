import copy
import glob
import numpy as np
import shapely as sh
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString
import matplotlib.pyplot as plt


TRACK_NAME = 'reinvent_base'

waypoints = np.load("./tracks/%s.npy" % TRACK_NAME)
coordinates = np.array(waypoints[:,0:2])



diff_lines = np.diff(coordinates, axis=0)
line_distances = np.linalg.norm(diff_lines, axis=1)

threshold = 0.1
mask = np.hstack([True, line_distances > threshold])
coordinates = coordinates[mask]


center_line = LineString(coordinates)






inner_off_string = center_line.offset_curve(0.01)
new = LineString()

plt.scatter(x=coordinates[:,0], y=coordinates[:,1])
plt.show()

center_line_string = sh.LineString(center_line)
inner_off_string = sh.LineString(center_line_string.offset_curve(0.3))