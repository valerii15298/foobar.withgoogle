from itertools import combinations


def solution(num_nuns, num_required):
    # Your code here
    arr = [set() for i in range(num_nuns)]

    next_key = 0
    combs = combinations(range(num_nuns), num_required - 1)
    for keys_indexes in combs:
        all_keys = reduce(lambda a, b: a.union(b), arr)
        keys = set()
        for i in keys_indexes:
            keys = keys.union(arr[i])
        if keys == all_keys:
            for i in range(num_nuns):
                if i not in keys_indexes:
                    arr[i].add(next_key)
            next_key += 1

    all_keys = reduce(lambda a, b: a.union(b), arr)
    max_key = max(all_keys)
    arr = sorted(map(list, arr))
    for i in arr:
        for k in range(len(i)):
            i[k] = max_key - i[k]
    return sorted(list(map(sorted, arr)))


#print solution(5, 3)
