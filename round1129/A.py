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
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    res=0
    a.sort()
    p=0
    left=0
    while p<n:
        if a[p]<=res:
            left+=1
        if a[p]==res and left>=k:
            left-=k
            res+=1
        if a[p]>res:
            print(res)
            return
        p+=1
    print(res)
    return res


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()