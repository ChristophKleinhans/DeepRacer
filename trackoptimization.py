import shapely as sh
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from reinvent_2018_offset_05 import raceline

# Resave the adjusted waypoints
# ar = np.array(raceline)
# np.save('reinvent_2018_offset_05_adjusted.npy', raceline)


# Original track
waypoints = np.load('reinvent_base.npy')

center_line_orig = waypoints[:,0:2]
inner_border_orig = waypoints[:,2:4]
outer_border_orig = waypoints[:,4:6]

center_line_orig = sh.LineString(center_line_orig)
inner_border_orig = sh.LineString(inner_border_orig)
outer_border_orig = sh.LineString(outer_border_orig)

plt.plot(center_line_orig.xy[0], center_line_orig.xy[1], 'b--')
plt.plot(inner_border_orig.xy[0], inner_border_orig.xy[1], 'b')
plt.plot(outer_border_orig.xy[0], outer_border_orig.xy[1], 'b')


# Raceline
raceline = np.load('reinvent_2018_offset_05_adjusted.npy')
raceline = sh.LineString(raceline)

track_width = 1
center_line_orig = sh.LineString(center_line_orig)
inner_line_orig = sh.LineString(center_line_orig.offset_curve(track_width/2))
outer_line_orig = sh.LineString(center_line_orig.offset_curve(-track_width/2))



plt.plot(raceline.xy[0], raceline.xy[1])

plt.show()



