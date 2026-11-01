t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    inversion=0
    cnt0,cnt1=[],[]
    tmp=0
    for i in range(n):
        if a[i]==0:
            cnt0.append(tmp)
            inversion+=tmp
        else:
            tmp+=1
    tmp=0
    for i in range(n-1,-1,-1):
        if a[i]==1:
            cnt1.append(tmp)
        else:
            tmp+=1
    res=[inversion]
    p0,p1=0,0
    len0,len1=len(cnt0),len(cnt1)
    for i in range(len(s)):
        if inversion==0:
            res.append(0)
            continue
        if s[i]=='1':
            inversion-=cnt1[len1-1]-p0
            len1-=1
            p1+=1
            res.append(inversion)
        else:
            inversion-=cnt0[len0-1]-p1
            len0-=1
            p0+=1
            res.append(inversion)
    print(*res)