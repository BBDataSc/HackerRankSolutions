import math
import os
import random
import re
import sys


def DiagonalSum(arr):
    # Write your code here
    left_right = []
    right_left = []
    a = 0
    for i in range(len(arr)):
        left_right.append(arr[i][i])
    for i in range(len(arr), 0, -1):
        right_left.append(arr[a][i - 1])
        a += 1
    right_left = sum(right_left)
    left_right = sum(left_right)
    if right_left >= left_right:
        print(right_left - left_right)
    elif right_left <= left_right:
        print(left_right - right_left)


if __name__ == '__main__':
    x = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    w = [[6, 6, 7, -10, 9, -3, 8, 9, -1]
        , [9, 7, -10, 6, 4, 1, 6, 1, 1]
        , [-1, -2, 4, -6, 1, -4, -6, 3, 9]
        , [-8, 7, 6, -1, -6, -6, 6, -7, 2]
        , [-10, -4, 9, 1, -7, 8, -5, 3, -5]
        , [-8, -3, -4, 2, -3, 7, -5, 1, -5]
        , [-2, -7, -4, 8, 3, -1, 8, 2, 3]
        , [-3, 4, 6, -7, -7, -8, -3, 9, -6]
        , [-2, 0, 5, 4, 4, 4, -3, 3, 0]]
    DiagonalSum(w)
    DiagonalSum(x)
