#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i=0;i<n;i++)cin>>a[i];
    int f=1;
    ll res=0;
    for(auto x:a){
        res+=x;
        if(x!=1){
            f=0;
        }
    }
    if(f){cout<<-1<<endl;return;}
    cout<<res-1<<endl;
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