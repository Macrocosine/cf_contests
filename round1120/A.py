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
    n=input()
    a=list(map(int,input().split()))
    cnt0,cnt1=a.count(0),a.count(1)
    if cnt1>=cnt0:
        print("Bessie")
    else:
        print("Elsie")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()