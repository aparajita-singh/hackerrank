#!/bin/python3
# PROBLEM STATEMENT: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# Given an array of values and a number d, rotate the elements of the array in anticlockwise direction, i.e.,
# from right to left, d number of times.

import os


# Complete the rotLeft function below.
def rotLeft(a, d):
    final = [a[i + d] for i in range(len(a)) if i + d < len(a)]
    [final.append(a[i]) for i in range(d)]
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
