#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MOD = 1000000007;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // forbidden 区间
    vector<int> diff(n + 1, 0);

    for (int i = 0; i < n; i++) {
        ll k = i + 1;

        int l = min<ll>(1LL * a[i] * k, n);
        int r = min<ll>(1LL * (a[i] + 1) * k, n);

        diff[l]++;
        diff[r]--;
    }

    vector<int> nums;
    int cur = 0;

    for (int i = 0; i < n; i++) {
        cur += diff[i];

        if (cur == 0) {
            nums.push_back(i);
        }
    }

    // best[l] = 左端点为 l 的 required interval 中最小的右端点
    vector<int> best(n, n);

    for (int i = 0; i < n; i++) {
        int k = i + 1;

        int end = min<ll>(1LL * a[i] * k, n);

        for (int l = 0; l < end; l += k) {
            int r = min(l + k - 1, n - 1);
            best[l] = min(best[l], r);
        }
    }

    // 删除包含其他区间的大区间
    vector<pair<int, int>> limit;

    for (int l = 0; l < n; l++) {
        if (best[l] == n) {
            continue;
        }

        int r = best[l];

        while (!limit.empty() && limit.back().second >= r) {
            limit.pop_back();
        }

        limit.push_back({l, r});
    }

    int m = limit.size();

    vector<int> dp(m + 1, 0);

    dp[0] = 1;

    int pre = 1;
    int l = 0, r = 0;

    for (int x : nums) {
        while (l < m && limit[l].second < x) {
            pre -= dp[l];

            if (pre < 0) {
                pre += MOD;
            }

            l++;
        }

        while (r < m && limit[r].first <= x) {
            r++;
        }

        dp[r] += pre;

        if (dp[r] >= MOD) {
            dp[r] -= MOD;
        }

        pre = 2LL * pre % MOD;
    }

    cout << dp[m] << '\n';
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