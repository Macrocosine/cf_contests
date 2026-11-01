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
    n = int(input())
    a = sorted(map(int, input().split()))

    mid = a[n // 2]
    res1 = sum(abs(x - mid) for x in a)
    res2 = a[-1] - a[0]

    print(res1, res2)
        
    

def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()