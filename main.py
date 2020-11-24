import math


def solution(dimensions, my_position, guard_position, distance):
    x_room, y_room = dimensions

    x_count_mirrors = int(math.ceil(float(distance) / x_room)) + 3
    y_count_mirrors = int(math.ceil(float(distance) / y_room)) + 3
    distance = distance ** 2

    def get_mirrors(position):
        x_mirrors = set()
        y_mirrors = set()

        x, y = position

        left, right = 2 * x, 2 * (x_room - x)
        x_left, x_right = x, x
        for i in range(x_count_mirrors):
            x_mirrors.add((x_left, y))
            x_mirrors.add((x_right, y))
            x_left -= left
            x_right += right
            left, right = right, left

        # print list(x_mirrors)

        for x_pos, y_pos in x_mirrors:
            down, up = 2 * y, 2 * (y_room - y)
            y_down, y_up = y, y
            for i in range(y_count_mirrors):
                y_mirrors.add((x_pos, y_down))
                y_mirrors.add((x_pos, y_up))
                y_down -= down
                y_up += up
                down, up = up, down

        # print list(y_mirrors)

        return x_mirrors.union(y_mirrors)

    my_mirrors = get_mirrors(my_position)
    guard_mirrors = get_mirrors(guard_position)

    corners = set()
    for i in range(x_count_mirrors):
        for j in range(y_count_mirrors):
            w, h = i * x_room, j * y_room
            corners.add((w, h))
            corners.add((-w, h))
            corners.add((w, -h))
            corners.add((-w, -h))

    def get_distance(pos1, pos2):
        return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2

    def is_between(a, b, c):
        crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
        if abs(crossproduct) != 0:
            return False

        hypo = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        dot_product = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1]) * (b[1] - a[1])
        if dot_product < 0:
            return False

        if dot_product > hypo:
            return False

        return True

    def check(g_pos):
        if get_distance(my_position, g_pos) > distance:
            return False

        for pos in (my_mirrors.union(guard_mirrors)).union(corners):
            if list(pos) not in (list(g_pos), my_position) and is_between(my_position, g_pos, pos):
                return False

        return True

    result_count = 0
    for guard_pos in guard_mirrors:
        if check(guard_pos):
            result_count += 1
            # print guard_pos

    if (tuple(guard_position) in corners) and (get_distance(my_position, guard_position) <= distance):
        result_count += 1

    return result_count


tests = [
    ([3, 2], [1, 1], [2, 1], 4),
    ([300, 275], [150, 150], [185, 100], 500),
    ([300, 275], [150, 150], [185, 100], 500)
]
res = solution(*tests[0])
print res

# def test():
#     for i in range(100):
#         x_room = random.randint()
#
# (415, -100)
# (-185, -100)
# (-185, 450)
# (415, 450)
#
#
# (415, -250)
# (415, 300)
# (-185, 300)
