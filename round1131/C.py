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
    n=int(input())
    a=list(map(int,input().split()))
    if a==[1]*n:
        print(-1)
        return
    if a.count(1)==n-1 and (a[0]!=1 or a[n-1]!=1):
        print(max(a[0],a[n-1]))
        return
    if a.count(1)==n-2 and(a[0]!=1 and a[n-1]!=1):
        print(a[0]+a[n-1]-1)
        return
    print(sum(a)-1)


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()