# def solution(L):
#     arrays = [[], [], []]
#     for i in L:
#         arrays[i % 3].append(i)
#
#     arr1rem = len(arrays[1]) % 3
#     arrays[0] += arrays[1][:len(arrays[1]) - arr1rem]
#     del arrays[1][:len(arrays[1]) - arr1rem]
#
#     arr2rem = len(arrays[2]) % 3
#     arrays[0] += arrays[2][:len(arrays[2]) - arr2rem]
#     del arrays[2][:len(arrays[2]) - arr2rem]
#
#     arr_rem = min(arr1rem, arr2rem)
#     if arr_rem != 0:
#         arrays[0] += arrays[1][-arr_rem:] + arrays[2][-arr_rem:]
#
#     return int(''.join(map(str, reversed(sorted(arrays[0])))))
#
#
# print solution([3, 1, 4, 1])


# def solution(start, length):
#     def xorsum(n):
#         if n == 0:
#             return 0
#
#         if (n - 1) % 4 == 0:
#             return n - 1
#         elif (n - 1) % 4 == 1:
#             return 1
#         elif (n - 1) % 4 == 2:
#             return n
#         else:
#             return 0
#
#     checksum = 0
#     cur = start
#     cur_len = length
#     while cur_len > 0:
#         checksum ^= xorsum(cur) ^ xorsum(cur + cur_len)
#         cur += length
#         cur_len -= 1
#
#     return checksum
#
#
# print solution(0, 3)
# print solution(17, 4)
# # print solution(200000, 25000)
# # 829043456
#
#
# def answer(start, length):
#     worker_list = [(start + (length - l) * length, start + (length - l) * length + l) for l in range(length, 0, -1)]
#
#     def getXOR(start, end):
#         if (end - start) == 0:
#             return 0
#         if (end - start) == 1:
#             return start
#         if (end - start) <= 4:
#             return reduce(lambda x, y: x ^ y, range(start, end))
#         else:
#             # if (start / 4 * 4 + 4) != (start + 4):
#             #     print start
#             begin_range = (start, start / 4 * 4 + 4)
#             end_range = (end / 4 * 4, end)
#             if (end / 4 * 4) != end:
#                 print end, (end / 4 * 4)
#             return getXOR(*begin_range) ^ getXOR(*end_range)
#
#     new_xor = [getXOR(start, end) for start, end in worker_list]
#
#     return reduce(lambda x, y: x ^ y, new_xor)


# print(answer(0, 3))
# print(answer(17, 4))
# print(answer(200000, 25000))

# max_n = 10000
# for id in range(max_n):
#     for length in range(1, max_n - id + 1):
#         if (solution(id, length) != answer(id, length)):
#             print "BAD: ", id, length
#             exit(-1)
#     print "Success: ", id

