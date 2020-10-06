from matplotlib.patches import Polygon
import numpy as np


def line_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    """ Calculates the intersection between two line segments.

    Args:
        x1: x coordinate of the first point in the first line segment as float
        y1: y coordinate of the first point in the first line segment as float
        x2: x coordinate of the second point in the first line segment as float
        y2: y coordinate of the second point in the first line segment as float
        x3: x coordinate of the first point in the second line segment as float
        y3: y coordinate of the first point in the second line segment as float
        x4: x coordinate of the second point in the second line segment as float
        y5: y coordinate of the second point in the second line segment as float

    Returns:
        Two floats representing the intersection between the to line segments.
        If they both are between 0 and 1, the line segments intersect within their bounds.
        returns None if lines are parralell
    """
    denominator = (x4-x3)*(y1-y2) - (x1-x2)*(y4-y3)
    if denominator == 0:
        print("Parralelle linjer møtes ikke...")
        return 9999999, 9999999

    ta = ((y3-y4)*(x1-x3) + (x4-x3)*(y1-y3)) / denominator
    tb = ((y1-y2)*(x1-x3) + (x2-x1)*(y1-y3)) / denominator
    return ta, tb


def get_angle_to_points(origin_x, origin_y, points_x, points_y):
    """ Get angles from some point to others

    numpy.arctan2() returns angle values from -pi to pi, so in a normal cartesian coordiante system
    with positive x going right, and positive y going up, the points are sorted counter clockwise
    starting from an angle of pi.

    Args:
        origin_x: x value of the origon coordinate as float
        origin_y: y value of the origon coordinate as float
        points_x: numpy array of floats with the x values of the points
        points_y: numpy array of floats with the y values of the points

    Returns:
        numpy array of floats containing the angles in radians.
    """
    points_delta_x = points_x - origin_x
    points_delta_y = points_y - origin_y
    return np.arctan2(points_delta_y, points_delta_x)


def get_closest_intersection(origin_x, origin_y, i, points_x, points_y, connections):
    smallest_ta = 9999999999
    checked = [i]

    for j, neighbors in enumerate(connections):
        if j != i:
            for k in neighbors:
                if k not in checked:
                    ta, tb = line_segment_intersection(origin_x, origin_y,
                                                       points_x[i], points_y[i],
                                                       points_x[j], points_y[j],
                                                       points_x[k], points_y[k])
                    # if the wall is somewhere on the line
                    if tb >= 0 and tb <= 1:
                        # if the wall is in front of us
                        if ta > 0:
                            # if the wall is blocking our point
                            if ta < 1:
                                return None
                            elif ta < smallest_ta:
                                smallest_ta = ta
            checked.append(j)
    return smallest_ta


def get_vision_polygon(origin_x, origin_y, points_x, points_y, connections):
    polygon_corners_x = []
    polygon_corners_y = []

    angles = get_angle_to_points(origin_x, origin_y, points_x, points_y)
    i_sorted = np.argsort(angles)

    for i in i_sorted:
        smallest_ta = get_closest_intersection(
            origin_x, origin_y, i, points_x, points_y, connections)
        if smallest_ta is not None:
            # If there is only one connection:
            if len(connections[i]) == 1:
                back_x = origin_x * (1-smallest_ta) + points_x[i]*smallest_ta
                back_y = origin_y * (1-smallest_ta) + points_y[i]*smallest_ta

                relative_angle = angles[connections[i][0]] - angles[i]
                if relative_angle > np.pi:
                    relative_angle -= 2*np.pi
                elif relative_angle < -np.pi:
                    relative_angle += 2*np.pi

                if relative_angle < 0:
                    polygon_corners_x.append(points_x[i])
                    polygon_corners_y.append(points_y[i])
                    polygon_corners_x.append(back_x)
                    polygon_corners_y.append(back_y)
                else:
                    polygon_corners_x.append(back_x)
                    polygon_corners_y.append(back_y)
                    polygon_corners_x.append(points_x[i])
                    polygon_corners_y.append(points_y[i])
            # If there are two connections:
            else:
                first_relative_angle = angles[connections[i][0]] - angles[i]
                if first_relative_angle > np.pi:
                    first_relative_angle -= 2*np.pi
                elif first_relative_angle < -np.pi:
                    first_relative_angle += 2*np.pi
                first_neighbor_is_before = \
                    first_relative_angle < 0

                second_relative_angle = angles[connections[i][1]] - angles[i]
                if second_relative_angle > np.pi:
                    second_relative_angle -= 2*np.pi
                elif second_relative_angle < -np.pi:
                    second_relative_angle += 2*np.pi
                second_neighbor_is_before = \
                    second_relative_angle < 0

                # If the neighboring points are on both sides of the current point
                if first_neighbor_is_before ^ second_neighbor_is_before:
                    print("here")
                    polygon_corners_x.append(points_x[i])
                    polygon_corners_y.append(points_y[i])
                else:
                    back_x = \
                        origin_x * (1-smallest_ta) + points_x[i]*smallest_ta
                    back_y = \
                        origin_y * (1-smallest_ta) + points_y[i]*smallest_ta
                    if first_neighbor_is_before and second_neighbor_is_before:
                        polygon_corners_x.append(points_x[i])
                        polygon_corners_y.append(points_y[i])
                        polygon_corners_x.append(back_x)
                        polygon_corners_y.append(back_y)
                    else:
                        polygon_corners_x.append(back_x)
                        polygon_corners_y.append(back_y)
                        polygon_corners_x.append(points_x[i])
                        polygon_corners_y.append(points_y[i])

    return polygon_corners_x, polygon_corners_y


if __name__ == "__main__":
    points_x = np.array([0, 5, 5, 0, 2, 1, 2, 3, 4])
    points_y = np.array([0, 0, 5, 5, 2, 3, 3, 3, 2])
    connections = [
        [3, 1],
        [0, 2],
        [1, 3],
        [2, 0],
        [5],
        [4],
        [7],
        [6, 8],
        [7]
    ]

    vision_origin_x = 2
    vision_origin_y = 4

    polygon_x, polygon_y = get_vision_polygon(
        vision_origin_x, vision_origin_y, points_x, points_y, connections
    )
    for i, point in enumerate(zip(polygon_x, polygon_y)):
        print(i+1, point)

    from testing_fov_animation import plot_fov

    plot_fov(vision_origin_x, vision_origin_y, points_x, points_y, connections)
