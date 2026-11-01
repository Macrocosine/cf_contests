#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 998244353;
ll calc(ll n) {
    if (n <= 1) return n;
    ll need = n - 1;
    ll sum = 0;
    ll ans = LLONG_MAX;
    for (int k = 60; k >= 2; k--) {
        if (need <= 0) {
            ans = min(ans, sum);
            break;
        }
        ll p = 1LL << k;
        ll w = p - 2;
        ll c = p + k - 1;
        if (need > p - 2LL * k) {
            sum += c;
            need -= w;
        } else {
            ans = min(ans, sum + c);
        }
    }
    if (need <= 0)
        ans = min(ans, sum);
    return ans - n;
}
void solve() {
    ll l, r;
    cin >> l >> r;

    ll ans = 0;

    for (ll n = l; n <= r; n++) {
        ans = (ans + calc(n)) % MOD;
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