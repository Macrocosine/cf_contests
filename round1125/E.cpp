#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int w(ll x, ll y) {
    return x == y ? 2 : 1;
}

void solve() {
    int n;
    cin >> n;
    vector<ll> a(n), b(n);
    for (ll &x : a) cin >> x;
    for (ll &x : b) cin >> x;
    vector<ll> suf(n);
    suf[n - 1] = w(a[n - 1], b[n - 1]);

    for (int i = n - 2; i >= 0; i--) {
        suf[i] = suf[i + 1]
               + w(a[i], b[i + 1])
               + w(a[i + 1], b[i]);
    }
    ll pre = 0;
    ll res = 0;
    for (int k = 0; k < n; k++) {
        res = max(res, pre + suf[k]);
        if (k + 1 < n) {
            pre += w(a[k], b[k]);
            pre += w(a[k + 1], b[k]);
        }
    }

    cout << res << '\n';
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