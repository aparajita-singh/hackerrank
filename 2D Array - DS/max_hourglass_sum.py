# !/bin/python3 PROBLEM STATEMENT: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#
# Given a 6x6 array, find all the valid hourglass arrays and their respective sums. Return the sum with the highest
# value.

import os

from functools import reduce

my_sum = lambda x, y: x + y


def get_hourglass(arr, r, c, h):
    return [arr[r + ri][c + ci] for ri in range(len(h)) for ci in h[ri] if is_valid_hourglass(arr, r, r + ri, c + ci)]


def hourglass_exists(arr, r, c, h):
    hourglass_count = reduce(my_sum, [1 for r in h for c in r])
    my_hourglass = get_hourglass(arr, r, c, h)
    return len(my_hourglass) is hourglass_count


def is_valid_hourglass(arr, r, rr, cc):
    return rr < len(arr) and cc < len(arr[r])


def do_sum(arr, r, c, h):
    # print(str(hourglass_count))
    my_hourglass = get_hourglass(arr, r, c, h)
    return reduce(my_sum, my_hourglass, 0)


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglassIndices = [[0, 1, 2], [1], [0, 1, 2]]
    final = [do_sum(arr, r, c, hourglassIndices) for r in range(len(arr)) for c in range(len(arr[r])) if
             hourglass_exists(arr, r, c, hourglassIndices)]
    print(final)
    return max(final)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
