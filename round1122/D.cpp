#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int res=1;
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i] -= i;
    }
    int tmp=1;
    sort(a.begin(), a.end());
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i - 1]+1) {
            tmp++;
            res = max(res, tmp);  
        } 
        else if (a[i] == a[i - 1]) {
            // Do nothing, duplicates are allowed
        }
        else {
            tmp = 1;
        }
    }
    cout << res << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}