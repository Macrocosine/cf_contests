t=int(input())
for _ in range(t):
    n=int(input())
    a=[-1]*n
    b=list(map(int,input().split()))
    diff=[0]*(n+1)
    for i in range(n):
        if b[i]!=-1 and b[i]!=0:
            l=max(0,i-b[i]+1)
            r=min(n-1,i+b[i]-1)
            diff[l]+=1
            diff[r+1]-=1
    cur=0
    for i in range(n):
        cur+=diff[i]
        if cur>0:
            a[i]=0
        else:
            a[i]=1
    f=1
    for i in range(n):
        if b[i]!=-1:
            if (i-b[i]>=0 and a[i-b[i]]) or (i+b[i]<n and a[i+b[i]]):
                continue
            else:
                f=0
                print(-1)
                break
    if f:
        print("".join(map(str,a)))