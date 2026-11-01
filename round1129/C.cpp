#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> tr(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        tr[x].push_back(y);
        tr[y].push_back(x);
    }

    vector<int> vis(n + 1);
    vector<int> flag(n + 1);
    vector<int> dist(n + 1);

    int cnt = 0;
    deque<pair<int, int>> q;
    q.push_back({n, 0});
    vis[n] = 1;
    flag[1] = 1;

    while (!q.empty()) {
        cnt += 1;
        int tmp = q.size();

        for (int i = 0; i < tmp; i++) {
            int x = q.front().first;
            int f = q.front().second;
            q.pop_front();

            if (x == 1) f = 1;

            for (auto y : tr[x]) {
                if (vis[y]) continue;
                vis[y] = 1;
                dist[y] = cnt;
                flag[y] = f;
                q.push_back({y, f});
            }
        }
    }

    int ans = dist[1];

    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (!flag[x])
            ans = max(ans, dist[x] + 1);
    }

    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}