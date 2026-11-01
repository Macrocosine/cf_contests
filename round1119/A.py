t=int(input())
ans=[]
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    res=0
    for j in range(0,len(s),k):
        f=1
        for p in range(j,j+k):
            if s[p]=='0':
                f=0
                break
        res+=f
    ans.append(res)
for i in ans:
    print(i)