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
    s=input()
    if s[0]=='1':
        print(s.count('0'))
    else:
        res,l,r=float(inf),0,n-1
        while l<n and s[l]=='0':
            l+=1
        while r>l and s[r]=='1':
            r-=1
        tmp=l
        cnt0,cnt1=0,0
        while tmp<=r:
            if s[tmp]=='0':
                cnt0+=1
            tmp+=1
        tmp=l
        while tmp<=r+1:
            res=min(res,cnt0+cnt1)
            if tmp<n and s[tmp]=='0':
                cnt0-=1
            else:
                cnt1+=1
            tmp+=1
        print(res)
def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()