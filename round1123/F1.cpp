#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int &x : a) cin >> x;

    vector<int> query(q);
    for (int &x : query) cin >> x;
    vector<int> res(60,0);
    res[0] = *max_element(a.begin(), a.end())- *min_element(a.begin(), a.end());
    for (int k = 1; k <= 60; k++) {
        if (res[k - 1] == 0) break;
        vector<int> tmp;
        tmp.reserve(1LL * n * (n - 1) / 2);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                tmp.push_back(a[i] ^ a[j]);
            }
        }
        sort(tmp.begin(), tmp.end());
        for (int i = 0; i < n; i++) {
            a[i] = tmp[i];
        }
        res[k] = a[n - 1] - a[0];
    }
    for (int x : query) {
        if (x >= 60)
            cout << 0 << '\n';
        else
            cout << res[x] << '\n';
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