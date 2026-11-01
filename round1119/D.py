t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = a.count(0)
    if cnt == 1:
        print("NO")
        continue

    print("YES")
    if cnt == 0:
        print("C" * n)
        continue
    res = ['C'] * n
    f = 0
    for i in range(n):
        if a[i] == 0:
            if f == 0:
                res[i] = 'A'
                f = 1
            else:
                res[i] = 'B'

    print(''.join(res))