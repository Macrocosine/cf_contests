#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int x, y, r;
    cin >> x >> y >> r;
    for (int i = -25; i <= 25; ++i) {
        for (int j = -25; j <= 25; ++j) {
            if ((x - i) * (x - i) + (y - j) * (y - j) == r * r) {
                cout << i << " " << j << "\n";
                return;
            }
        }
    }
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