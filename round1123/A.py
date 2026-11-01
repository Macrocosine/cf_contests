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
    n,c=input().strip().split()
    s=input().strip()
    n=int(n)
    l,r=0,n-1
    res=0
    while l<r:
        if s[l]!=s[r]:
            if s[l]!=c and s[r]!=c:
                res+=1
            res+=1
        l+=1
        r-=1
    print(res)
def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()