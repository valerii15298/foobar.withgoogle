def solution(dimensions, your_position, guard_position, distance):
    my_mirrors = []
    guard_mirrors = []
    x_room, y_room = dimensions
    x_my, y_my = your_position
    x_guard, y_guard = guard_position

    my_left = -2 * x_my
    my_right = 2 * (x_room - x_my)
    my_down = -2 * y_my
    my_up = 2 * (y_room - y_my)

    guard_left = -2 * x_guard
    guard_right = 2 * (x_room - x_guard)
    guard_down = -2 * y_guard
    guard_up = 2 * (y_room - y_guard)

    def do_mirror(arr_coordinates, sides):
        new_dots = set()
        for x, y in arr_coordinates:
            new_dots.add((x + sides[0], y))
            new_dots.add((x + sides[1], y))
            new_dots.add((x, y + sides[2]))
            new_dots.add((x, y + sides[3]))
        return new_dots


solution([3, 2], [1, 1], [2, 1], 4)
