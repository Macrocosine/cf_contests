#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i=0;i<n;i++)cin>>a[i];
    set<int>s;
    map<int,int>d;
    for(auto x:a){s.insert(x);d[x]+=1;}
    ll res1=0,res2=0;
    ll cnt=0;
    vector<int>na(s.begin(),s.end());
    for(int i=0;i+1<na.size();i++){
        int tmp=na[i+1]-na[i];
        cnt+=d[na[i]];
        res2+=tmp;
        if (2*cnt<n){res1+=cnt*tmp;}
        else{res1+=(n-cnt)*tmp;}
    }
    cout<<res1<<" "<<res2<<"\n";
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