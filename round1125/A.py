import sys

from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict, deque
from functools import cache, lru_cache
from heapq import heapify, heappop, heappush, heapreplace
from itertools import accumulate, combinations, permutations, product
from math import ceil, floor, gcd, inf, isqrt, lcm, sqrt

input = sys.stdin.readline
write = sys.stdout.write

sys.setrecursionlimit(1_000_000)


def solve():
    x,y,r = map(int, input().split())
    for i in range(-25, 26):
        for j in range(-25, 26):
            if (x-i)**2 + (y-j)**2 == r**2:
                print(i, j)
                return


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()