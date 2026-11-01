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
    cnt1,cnt2=0,0
    l1,l2=[],[]
    for i in range(0,n,2):
        if a[i]<0:
            cnt1+=1
        l1.append(a[i])
    for i in range(1,n,2):
            if a[i]<0:
                cnt2+=1
            l2.append(a[i])
    res=0
    l1.sort()
    l2.sort()
    p1,p2=0,0
    while p1<len(l1) and  p2<len(l2):
        if -l1[p1]-l2[p2]>l1[p1]+l2[p2]:
            res+=-l1[p1]-l2[p2]
        else:
            res+=l1[p1]+l2[p2]
        p1+=1
        p2+=1
    while p1<len(l1):
        res+=l1[p1]
        p1+=1
    while p2<len(l2):
        res+=l2[p2]
        p2+=1
    print(res)

    
         
        


def main():
    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()