from matplotlib import pyplot as plt
from shapely.geometry import LineString

# Init vectors
vector1x = [10, 15]
vector1y = [7, 15]

vector2x = [16, 12]
vector2y = [4, 15]

vector3x = [7, 9]
vector3y = [19, 2]

# Visualize vectors
plt.subplot(111, title="x - end")

plt.plot(vector1x, vector1y, color='b')
plt.plot(vector2x, vector2y, color='b')
plt.plot(vector3x, vector3y, color='b')

plt.plot(vector1x[0], vector1y[0], 's')
plt.plot(vector2x[0], vector2y[0], 's')
plt.plot(vector3x[0], vector3y[0], 's')

plt.plot(vector1x[1], vector1y[1], 'x')
plt.plot(vector2x[1], vector2y[1], 'x')
plt.plot(vector3x[1], vector3y[1], 'x')

# Create lines
line1 = LineString([[vector1x[0], vector1y[0]], [vector1x[1], vector1y[1]]])
line2 = LineString([[vector2x[0], vector2y[0]], [vector2x[1], vector2y[1]]])
line3 = LineString([[vector3x[0], vector3y[0]], [vector3x[1], vector3y[1]]])

# Calculate intersection
for line_seconde in [line1, line2, line3]:
    for line_first in [line1, line2, line3]:
        int_pt = line_first.intersection(line_seconde)
        try:
            point_of_intersection = int_pt.x, int_pt.y
            print(point_of_intersection)
            plt.plot(int_pt.x, int_pt.y, '*')
        except:
            pass

point = [3, 3]
plt.plot(point[0], point[1], 'x')


def is_right(line_point, line_point_2, point):
    return not (((line_point_2[0] - line_point[0]) * (point[1] - line_point[1]) - (line_point_2[1] - line_point[1]) * (
            point[0] - line_point[0])) > 0)


# Is right make vector red
if is_right([vector1x[0], vector1y[0]], [vector1x[1], vector1y[1]], point):
    plt.plot(vector1x, vector1y, color='r')

if is_right([vector2x[0], vector2y[0]], [vector2x[1], vector2y[1]], point):
    plt.plot(vector2x, vector2y, color='r')

if is_right([vector3x[0], vector3y[0]], [vector3x[1], vector3y[1]], point):
    plt.plot(vector3x, vector3y, color='r')

plt.show()
