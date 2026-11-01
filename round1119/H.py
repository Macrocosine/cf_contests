from functools import cache
t=int(input())
mod=1000000007
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
        elif b[i]==0:
            a[i]=1
    f=1
    for i in range(n):
        if b[i]!=-1:
            if (i-b[i]>=0 and a[i-b[i]]==1) or (i+b[i]<n and a[i+b[i]]==1):
                continue
            elif(i-b[i]>=0 and a[i-b[i]]==-1) and (i+b[i]<n and a[i+b[i]]==-1):
                continue
            elif (i-b[i]>=0 and a[i-b[i]]==-1) and (i+b[i]>=n or (i+b[i]<n and a[i+b[i]]==0)):
                a[i-b[i]]=1
                continue
            elif (i+b[i]<n and a[i+b[i]]==-1) and (i-b[i]<0 or (i-b[i]>=0 and a[i-b[i]]==0)):
                a[i+b[i]]=1
                continue
            else:
                f=0
                print(0)
                break
    candidates=[]
    tmp=-1
    cnt=0
    for i in range(n):
        if b[i]!=-1 and b[i]!=0:
            if (i-b[i]>=0 and a[i-b[i]]==-1) and (i+b[i]<n and a[i+b[i]]==-1):
                l,r=i-b[i],i+b[i]
                if cnt==0:
                    cnt=1
                elif l==tmp:
                    cnt+=1
                else:
                    candidates.append(cnt)
                    cnt=1
                tmp=r
    if cnt!=0:
        candidates.append(cnt)
    if f:
        m=a.count(-1)
        if m==n:
            res=(pow(2,n,mod)-1)%mod
            print(res)
        else:
            @cache
            def dfs(n):
                if n == 0:
                    return 1
                f0, f1 = 1,2
                for _ in range(2, n + 1):
                    f0, f1 = f1%mod, (f1 + f0)%mod
                return f1
            res=1
            for x in candidates:
                res=res*dfs(x+1)%mod
                m-=x+1
            res=res*pow(2,m,mod)%mod
            print(res)

