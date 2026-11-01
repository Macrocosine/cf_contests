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
    if k>2*n-1 or k<n:
        print(-1)
    else:
        ans=[[0]*n for _ in range(n)]
        for i in range(k-n+1):
            ans[i][0]=i+1
        for i in range(2*n-k-1):
            ans[i+k-n+1][i+k-n+1]=i+k-n+2
        p=n+1
        for i in range(n):
            for j in range(n):
                if ans[i][j]==0:
                    ans[i][j]=p
                    p+=1
        for row in ans:
            print(*row)
def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()