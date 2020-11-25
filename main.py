from itertools import product
import fractions


def solution(dimensions, my_position, guard_position, distance):
    def gen_list(length, shift, pos):
        end = length + distance + 1
        step = 2 * length
        result1 = set(range(pos, end, step)).union(range(pos + 2 * (length - shift), end, step))
        result2 = set(range(pos, -end, -step)).union(range(pos - 2 * shift, -end, -step))
        return result1.union(result2)

    def get_list(shifts, position):
        x_list = gen_list(dimensions[0], shifts[0], position[0])
        y_list = gen_list(dimensions[1], shifts[1], position[1])
        return set(product(x_list, y_list))

    my_mirrors = get_list(my_position, (0, 0))

    guard_shifts = guard_position[:]
    guard_position = (guard_position[0] - my_position[0], guard_position[1] - my_position[1])

    guard_mirrors = get_list(guard_shifts, guard_position)

    corners = get_list((0, 0), (- my_position[0], - my_position[1]))

    def store(x, y, visited):
        gcd = fractions.gcd(abs(x), abs(y))
        visited.add((x/gcd, y/gcd))

    distance = distance ** 2

    def get_distance(pos):
        return pos[0] ** 2 + pos[1] ** 2

    def is_between(b, c):
        cross = c[1] * b[0] - c[0] * b[1]
        if cross != 0:
            return False

        hypo = b[0] ** 2 + b[1] ** 2

        dot_product = c[0] * b[0] + c[1] * b[1]
        if dot_product < 0:
            return False

        if dot_product > hypo:
            return False

        return True

    def check(g_pos):
        if get_distance(g_pos) > distance:
            return False

        for pos in (my_mirrors.union(guard_mirrors)).union(corners):
            if pos not in (g_pos, (0, 0)) and is_between(g_pos, pos):
                return False

        return True

    result_count = 0
    for guard_pos in guard_mirrors:
        if check(guard_pos):
            result_count += 1
            # print guard_pos

    if (guard_position in corners) and (get_distance(guard_position) <= distance):
        result_count += 1

    return result_count


tests = [
    ([3, 3], [1, 1], [2, 1], 10),
    ([3, 2], [1, 1], [2, 1], 4),
    ([300, 275], [150, 150], [185, 100], 500),
    ([3, 2], [1, 1], [2, 1], 10000)
]
res = solution([300, 200], [100, 100], [200, 100], 10000)
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
