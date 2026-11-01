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
    b=[0]*101
    for x in a:
        b[x]+=1
    res=[]
    while len(res)<len(a):
        for x in range(100,0,-1):
            if b[x]!=0:
                b[x]-=1
                res.append(str(x))
    print(" ".join(res))


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()