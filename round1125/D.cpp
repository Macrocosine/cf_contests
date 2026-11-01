#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    ll k;
    cin >> n >> k;

    vector<pair<ll, ll>> a;
    vector<ll> b;

    for (int i = 0; i < n; i++) {
        ll x, y, z;
        cin >> x >> y >> z;

        if (x == y && y == z) {
            b.push_back(x + y + z);
        } else if (x <= y && y <= z) {
            a.push_back({x + y + z, 2 + 2 * min(y - x, z - y)});
        } else {
            a.push_back({x + y + z, 0});
        }
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    if (a.empty()) {
        cout << b[0] << '\n';
        return;
    }

    const ll INF = 4e18;

    ll min_b = b.empty() ? INF : b[0];
    ll cur = a[0].first;

    if (cur >= min_b) {
        cout << min_b << '\n';
        return;
    }

    int m = a.size();
    int i = 0;
    ll cnt = 0;

    while (true) {
        ll extra = 0;

        while (i < m && a[i].first == cur) {
            extra += a[i].second;
            cnt++;
            i++;
        }

        ll nxt = min_b;
        if (i < m) nxt = min(nxt, a[i].first);

        if (nxt == INF) {
            if (k < extra) {
                cout << cur << '\n';
                return;
            }

            k -= extra;
            cur += k / cnt;
            cout << cur << '\n';
            return;
        }

        if (k < extra) {
            cout << cur << '\n';
            return;
        }

        k -= extra;

        ll d = nxt - cur;

        if (d > k / cnt) {
            cur += k / cnt;
            cout << cur << '\n';
            return;
        }

        k -= cnt * d;
        cur = nxt;

        if (cur == min_b) {
            cout << cur << '\n';
            return;
        }
    }
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