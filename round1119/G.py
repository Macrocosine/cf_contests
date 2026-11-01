from bisect import bisect
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dist = [a[i] - a[i-1] for i in range(1, n)]
    c = [k - x for x in dist]
    p = [0] * n
    wp = [0] * n#weighted_prefix
    for i in range(n - 1):
        p[i+1] = p[i] + c[i]
        wp[i+1] = wp[i] + i * c[i]
    res = [0]
    for i in range(1, n - 1):
        req = max(0, dist[i] + dist[i-1] - k)
        if req == 0:
            res.append(0)
            continue
        index = bisect(p, req + p[i+1], lo=i+1)-(i+1)
        R = i + index - 1
        if R >= i + 1:
            s = p[R+1] - p[i+1]
            ans = (wp[R+1] - wp[i+1]) - i * s
            req -= s
        else:
            ans = 0
        ans += req * index
        res.append(ans)

    res.append(0)
    print(*res)