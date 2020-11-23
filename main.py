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


# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
