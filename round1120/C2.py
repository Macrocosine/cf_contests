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
    mod=1000000007
    n=int(input())
    a=list(map(int,input().split()))
    diff=[0]*(n+1)
    for i in range(n):
        diff[min(a[i]*(i+1),n)]+=1
        diff[min((a[i]+1)*(i+1),n)]-=1
    cur=0
    nums=[]
    for i in range(n):
        cur-=diff[i]
        if cur>=0:
            nums.append(i)
    best = [n] * n
    for i in range(n):
        k = i + 1
        for l in range(0, min(a[i] * k, n), k):
            r = min(l + k - 1, n - 1)
            best[l] = min(best[l], r)
    limit = []
    for l in range(n):
        if best[l] == n:
            continue
        r = best[l]
        while limit and limit[-1][1] >= r:
            limit.pop()
        limit.append((l, r))
    m=len(limit)
    l,r=0,0
    dp=[0]*(m+1)
    dp[0]=1
    pre=1
    for x in nums:
        while l<m and limit[l][1]<x:
            pre=(pre-dp[l])%mod
            l+=1
        while r<m and limit[r][0]<=x:
            r+=1
        dp[r]=(dp[r]+pre)%mod
        pre=(pre+pre)%mod
    print(dp[m])

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()