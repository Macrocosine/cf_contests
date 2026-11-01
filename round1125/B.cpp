#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> ans(n, 0);
    vector<int> stk;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            stk.push_back(i);
        }
        else if(s[i]=='2'){
            if (!stk.empty()) {
                ans[stk.back()] = 1;
                stk.pop_back();
            }
            else{
                ans[i] = 1;
            }
        }
        else{
            ans[i] = 1;
        }
    }
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (ans[i] == 0) {
            cnt++;
        }
    }
    cout << cnt << "\n";
    for (int i = 0; i < n; ++i) {
        if (ans[i]==0) {
            cout << i+1 << " ";
        }
    }
    cout << "\n";
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