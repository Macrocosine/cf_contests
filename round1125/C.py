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
    a = list(map(int, input().split()))
    d1 = defaultdict(int)
    for i in range(4,n):
        tmp=-a[i]+a[i-2]+a[i-4]
        d1[tmp]+=1
    res=0
    for k in d1.keys():
        res+=d1[k]*(d1[k]-1)//2
    for i in range(4,n):
        tmp1=-a[i]+a[i-2]+a[i-4]
        if i+2<n:
           tmp2=-a[i+2]+a[i]+a[i-2]
           if tmp1==tmp2:
               res-=1
        if i+4<n:
            tmp2=-a[i+4]+a[i+2]+a[i]
            if tmp1==tmp2:  
                res-=1
    print(res) 


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()