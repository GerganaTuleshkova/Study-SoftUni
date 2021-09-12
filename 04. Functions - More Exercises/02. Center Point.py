from math import sqrt
from math import floor


def closer_point(x_p1, y_p1, x_p2, y_p2):
    distance_p1_to_center = sqrt((x_p1 ** 2) +(y_p1 ** 2))
    distance_p2_to_center = sqrt((x_p2 ** 2) +(y_p2 ** 2))

    if distance_p1_to_center <= distance_p2_to_center:
        return f"({floor(x_p1)}, {floor(y_p1)})"
    else:
        return f"({floor(x_p2)}, {floor(y_p2)})"


x_p_1 = float(input())
y_p_1 = float(input())
x_p_2 = float(input())
y_p_2 = float(input())
print(closer_point(x_p_1, y_p_1, x_p_2, y_p_2))