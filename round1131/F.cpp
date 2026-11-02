
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll mod = 998244353;

void solve() {
    int n, m;
    cin >> n >> m;
    int mx = m + 2;
    vector<ll> dp(mx + 1), pre(mx + 1);
    dp[mx] = 1;
    for (int k = 1; k < n; k++) {
        pre[0] = 0;
        for (int i = 1; i <= mx; i++) {
            pre[i] = (pre[i-1] + dp[i]) % mod;
        }

        vector<ll> ndp(mx + 1);

        for (int a = 1; a <= mx; a++) {
            int r = min(mx, 2 * a - 1);

            ndp[a] = (pre[r] - pre[a-1] + mod) % mod;

            if (a == 1) {
                ndp[a] = (ndp[a] + dp[2]) % mod;
            }
        }

        dp.swap(ndp);
    }

    cout << (dp[1] + dp[2]) % mod << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) solve();

    return 0;
}
