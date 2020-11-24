import math
from fractions import Fraction as f


def solution(dimensions, my_position, guard_position, distance):
    distance = distance ** 2
    x_room, y_room = dimensions

    x_count_mirrors = int(math.ceil(float(distance) / x_room))
    y_count_mirrors = int(math.ceil(float(distance) / y_room))

    def get_mirrors(position):
        x_mirrors = set()
        y_mirrors = set()
        x, y = position
        left = 2 * x
        right = 2 * (x_room - x)
        x_left, x_right = x, x
        for i in range(x_count_mirrors):
            x_left -= left
            x_right += right
            x_mirrors.add((x_left, y))
            x_mirrors.add((x_right, y))
            left, right = right, left

        # print list(x_mirrors)

        down = 2 * y
        up = 2 * (y_room - y)

        for x_pos, y_pos in x_mirrors:
            y_down, y_up = y, y
            for i in range(y_count_mirrors):
                y_down -= down
                y_up += up
                y_mirrors.add((x_pos, y_down))
                y_mirrors.add((x_pos, y_up))
                y_down, y_up = y_up, y_down

        # print list(y_mirrors)

        return x_mirrors.union(y_mirrors)

    my_mirrors = get_mirrors(my_position)
    guard_mirrors = get_mirrors(guard_position)

    def get_distance(pos1, pos2):
        return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2

    def is_between(b, c):
        distance = 25

        crossproduct = c[1] * b[0] - c[0] * b[1]
        if abs(crossproduct) != 0:
            return False

        hypo = b[0] ** 2 + b[1] ** 2

        if hypo < distance:
            k = f(b[0], b[1]) ** 2
            bx2 = f(distance, (1 / k) + 1)
            by2 = f(distance, k + 1)

            bx = math.sqrt(bx2) * (1 if b[0] >= 0 else -1)
            by = math.sqrt(by2) * (1 if b[1] >= 0 else -1)

            hypo = bx2 + by2
            assert hypo == distance

            if (c[0] * bx + c[1] * by) < 0:
                return False

            c = list(c)
            c[0] = c[0] ** 2
            c[1] = c[1] ** 2

            l = ((c[0] * bx2) + (c[1] * by2) - (hypo ** 2)) ** 2
            r = 4 * c[0] * c[1] * bx2 * by2

            if l < r:
                return False

        else:
            dot_product = c[0] * b[0] + c[1] * b[1]
            if dot_product < 0:
                return False

            if dot_product > hypo:
                return False

        return True

    r = is_between((1, 1), (2, 2))
    print r
    return 0

    def check(pos1, pos2):
        if get_distance(pos1, pos2) > distance:
            return False
        for my_pos in my_mirrors:
            if is_between(pos1, pos2, my_pos):
                return False
        return True

    result_count = 0
    for guard_pos in guard_mirrors:
        if check(my_position, guard_position):
            result_count += 1

    return result_count


res = solution([3, 2], [1, 1], [2, 1], 4)
# print res

# x1, y1 = (3.0, 4.0)
# x2, y2 = (6.0, 8.0)
# d = 15.0
#
#
# y3 = d ** 2 / (((y2 - y1) / (x2 - x1)) ** 2 + 1)
#
# print y3
