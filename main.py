from itertools import product
import fractions
import math


def solution(dimensions, my_position, guard_position, distance):
    def gen_list(length, shift, pos):
        end = length + distance + 1
        step = 2 * length
        up = set(range(pos, end, step)).union(range(pos + 2 * (length - shift), end, step))
        down = set(range(pos, -end, -step)).union(range(pos - 2 * shift, -end, -step))
        return up | down

    def get_list(shifts, position):
        x_list = gen_list(dimensions[0], shifts[0], position[0])
        y_list = gen_list(dimensions[1], shifts[1], position[1])
        mirrors = {}
        for pos in product(x_list, y_list):
            hypo = math.hypot(*pos)
            if hypo <= distance:
                mirrors[pos] = hypo
        return mirrors

    my_mirrors = get_list(my_position, (0, 0))
    guard_mirrors = get_list(guard_position, (guard_position[0] - my_position[0], guard_position[1] - my_position[1]))
    corners = get_list((0, 0), (- my_position[0], - my_position[1]))

    dots = {}
    dots.update(my_mirrors)
    dots.update(guard_mirrors)
    dots.update(corners)
    dots = map(lambda x: x[0], sorted(dots.items(), key=lambda item: item[1]))

    guards = set(guard_mirrors)
    result_count = 0

    visited = set()
    for dot in dots:
        gcd = max(fractions.gcd(abs(dot[0]), abs(dot[1])), 1)
        angle = (dot[0] / gcd, dot[1] / gcd)
        if dot in guards and angle not in visited:
            result_count += 1
        visited.add(angle)

    return result_count


tests = [
    ([3, 2], [1, 1], [2, 1], 4),
    ([300, 275], [150, 150], [185, 100], 500),
    ([300, 200], [100, 100], [200, 100], 10000),
    ([30, 20], [10, 10], [20, 10], 10000),
    ([3, 2], [1, 1], [2, 1], 10000),
]

res = solution(*tests[3])
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
