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
    a,b,c=map(int,input().split())
    n=a+b+c
    if a==max(a,b,c):
        res=['P']*n
        print("".join(res))
    elif b==max(a,b,c):
        res=['R']*n
        print("".join(res))
    else:
        res=['S']*n
        print("".join(res))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()