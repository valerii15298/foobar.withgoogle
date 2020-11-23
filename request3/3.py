#recruitme command


def solution(x, y):

    x, y = int(x), int(y)
    # 'x' is for Mach Bombs
    # 'y' is for Facula Bombs

    cycles = 0
    # Counts the number of replication cycles

    while (x != 1 and y != 1):

        # If number of Mach bombs and Facula bombs are same
        # Then, It is impossible to replicate to the desired
        # Total number of bombs

        if x % y == 0:
            return "impossible"

        else:
            # cycles = cycles + 1
            # ABOVE ASSIGNMENT, CAUSES TWO TEST CASES TO FAIL
            # FOR EXAMPLE FOR 7/3 : 2 CYCLES ARE CONSUMED
            cycles = cycles+int(max(x, y)/min(x, y))

            x, y = max(x, y) % min(x, y), min(x, y)

    return str(cycles+max(x, y)-1)