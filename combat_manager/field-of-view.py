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
        return None

    ta = ((y3-y4)*(x1-x3) + (x4-x3)*(y1-y3)) / denominator
    tb = ((y1-y2)*(x1-x3) + (x2-x1)*(y1-y3)) / denominator
    return ta, tb


def sort_points_by_angle(origin_x, orogin_y, points_x, points_y):
    """ Sorts points by the angle from an origin.

    numpy.arctan2() returns angle values from -pi to pi, so in a normal cartesian coordiante system
    with positive x going right, and positive y going up, the points are sorted counter clockwise
    starting from an angle of pi.

    Args:
        origin_x: x value of the origon coordinate as float
        origin_y: y value of the origon coordinate as float
        points_x: numpy array of floats with the x values of the points
        points_y: numpy array of floats with the y values of the points

    Returns:
        numpy array of integers containing the indices of the sorted angles.
    """
    points_delta_x = points_x - origin_x
    points_delta_y = points_y - origin_y
    angles = np.arctan2(points_delta_y, points_delta_x)
    return np.argsort(angles)


def get_vision_polygon(origin_x, origin_y, points_x, points_y, walls):
    polygon_corners_x = []
    polygon_corners_y = []

    i_sorted = sort_points_by_angle(origin_x, origin_y, points_x, points_y)
    for i in i_sorted:
        not_blocked = True
        back_walls = {}

        for p1, p2 in walls:
            ta, tb = line_segment_intersection(origin_x, origin_y,
                                               points_x[i], points_y[i],
                                               p1[0], p1[1],
                                               p2[0], p2[1])
            # if the wall is somewhere on the line
            if tb >= 0 and tb <= 1:
                # if the wall is in front of us
                if ta >= 0:
                    # if the wall is blocking our point
                    if ta <= 1:
                        not_blocked = False
                        break
                    back_walls[p1, p2] = ta

        if not_blocked:


if __name__ == "__main__":
    x1, y1, x2, y2 = 2., 2., 3., 3.
    x3, y3, x4, y4 = 3., 4., 4., 3.
    print(line_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4))
