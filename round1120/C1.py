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
    diff=[0]*(n+1)
    ans=[]
    for i in range(n):
        diff[min(a[i]*(i+1),n)]+=1
        diff[min((a[i]+1)*(i+1),n)]-=1
    cur=0
    for i in range(n):
        cur-=diff[i]
        if cur>=0:
            ans.append(i)
    print(len(ans))
    print(*ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()