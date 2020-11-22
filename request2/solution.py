def solution(l, t):
    length = len(l)
    for i in range(len(l)):
        if l[i] == 0:
            continue
        sum = 0
        start, end = i, i - 1
        while sum < t and end < length - 1:
            end += 1
            sum += l[end]
        if sum == t and start <= end:
            return [start, end]
    return [-1, -1]
