import math



def solution(dimensions, your_position, guard_position, distance):
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

    my_mirrors = get_mirrors(your_position)
    guard_mirrors = get_mirrors(guard_position)

    return 1

solution([5, 3], [1, 1], [2, 1], 6)
