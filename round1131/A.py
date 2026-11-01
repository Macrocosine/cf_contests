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
    n,m=map(int,input().split())
    s1=input()
    s2=input()
    f=1
    for i in range(0,26):
        x=chr(ord('a')+i)
        if x=='s' or x=='i' or x=='x':
            if s1.count(x)!=s2.count(x)+1:
                f=0
                break
        else:
            if s1.count(x)!=s2.count(x):
                f=0
                break
    if f:
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()