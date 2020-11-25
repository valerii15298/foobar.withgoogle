import itertools
import fractions


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
        distance2 = distance ** 2
        for pos in itertools.product(x_list, y_list):
            hypo = pos[0] ** 2 + pos[1] ** 2
            if hypo <= distance2:
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


# tests = {
#     ((3, 2), (1, 1), (2, 1), 4): 7,
#     ((300, 275), (150, 150), (185, 100), 500): 9,
#     ((300, 200), (100, 100), (200, 100), 10000): 3995,
#     ((30, 20), (10, 10), (20, 10), 10000): 397845,
# }
#
# for test, result in tests.items():
#     if solution(*test) != result:
#         print 'Test not passed!'
#     else:
#         print 'Test passed!'
