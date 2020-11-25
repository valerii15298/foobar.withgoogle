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
        if dot in guards and dot not in visited:
            result_count += 1
        gcd = fractions.gcd(abs(dot[0]), abs(dot[1]))
        if gcd == 0:
            gcd = 1
        visited.add((dot[0] / gcd, dot[1] / gcd))

    return result_count

    # def is_between(b, c):
    #     cross = c[1] * b[0] - c[0] * b[1]
    #     if cross != 0:
    #         return False
    #
    #     hypo = b[0] ** 2 + b[1] ** 2
    #
    #     dot_product = c[0] * b[0] + c[1] * b[1]
    #     if dot_product < 0:
    #         return False
    #
    #     if dot_product > hypo:
    #         return False
    #
    #     return True

    # def check(g_pos):
    #     if get_distance(g_pos) > distance:
    #         return False
    #
    #     for pos in (my_mirrors.union(guard_mirrors)).union(corners):
    #         if pos not in (g_pos, (0, 0)) and is_between(g_pos, pos):
    #             return False
    #
    #     return True

    # result_count = 0
    # for guard_pos in guard_mirrors:
    #     if check(guard_pos):
    #         result_count += 1
    #         # print guard_pos
    #
    # if (guard_position in corners) and (get_distance(guard_position) <= distance):
    #     result_count += 1

    # return result_count


tests = [
    ([3, 2], [1, 1], [2, 1], 4),
    ([300, 275], [150, 150], [185, 100], 500),
    ([3, 2], [1, 1], [2, 1], 10000),
    ([300, 200], [100, 100], [200, 100], 10000),
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
