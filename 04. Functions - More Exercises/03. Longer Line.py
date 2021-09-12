from math import sqrt
from math import floor


def closer_point(x_p1, y_p1, x_p2, y_p2):
    distance_p1_to_center = sqrt((x_p1 ** 2) +(y_p1 ** 2))
    distance_p2_to_center = sqrt((x_p2 ** 2) +(y_p2 ** 2))

    if distance_p1_to_center <= distance_p2_to_center:
        return f"({floor(x_p1)}, {floor(y_p1)})({floor(x_p2)}, {floor(y_p2)})"
    else:
        return f"({floor(x_p2)}, {floor(y_p2)})({floor(x_p1)}, {floor(y_p1)})"


def distance_between_points(x_p1, y_p1, x_p2, y_p2):
    side_a = x_p2 - x_p1
    side_b = y_p2 - y_p1
    distance = sqrt((side_a ** 2) + (side_b ** 2))
    return distance


def longer_line(x_p1, y_p1, x_p2, y_p2, x_p3, y_p3, x_p4, y_p4):
    line_1_length = distance_between_points(x_p1, y_p1, x_p2, y_p2)
    line_2_length = distance_between_points(x_p3, y_p3, x_p4, y_p4)
    if line_1_length >= line_2_length:
       formatted_result = closer_point(x_p1, y_p1, x_p2, y_p2)
    else:
        formatted_result = closer_point(x_p3, y_p3, x_p4, y_p4)
    return formatted_result


x_p_1 = float(input())
y_p_1 = float(input())
x_p_2 = float(input())
y_p_2 = float(input())
x_p_3 = float(input())
y_p_3 = float(input())
x_p_4 = float(input())
y_p_4 = float(input())
print(longer_line(x_p_1, y_p_1, x_p_2, y_p_2, x_p_3, y_p_3, x_p_4, y_p_4))