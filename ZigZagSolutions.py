import math
import os
import random
import re
import sys

'''
input:
    1
    7
    1 2 3 4 5 6 7

expected output:
    1 2 3 7 6 5 4

'''


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 1
    while (st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


if __name__ == '__main__':
    test_cases = int(input())
    for cs in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        findZigZagSequence(a, n)
