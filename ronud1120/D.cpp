#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct BIT{
    int n;
    vector<ll>tree;
    BIT(int n):n(n),tree(n+1,0){}
    void add(int x,ll v){
        while (x<=n){
        tree[x]+=v;
        x+=x&-x;
        }
    }
    ll sum(int x){
        ll res=0;
        while(x>0){
            res+=tree[x];
            x-=x&-x;
        }
        return res;
    }
    ll query(int l,int r){
        return sum(r)-sum(l-1);
    }
};
void solve() {
    int n;
    cin>>n;
    vector<ll>a(n+1);
    vector<int>p(n);
    ll x;
    for(int i=1;i<=n;i++)cin>>a[i];
    for(int i=0;i<n;i++)cin>>p[i];
    set<int>imp;
    vector<int>ans;
    BIT bit(n);
    for (int i =n-1;i>-1;i--){
        int k=p[i];
        bit.add(k, a[k]);
        auto it = imp.lower_bound(k);
        int root;
    if (it == imp.begin()) {
        imp.insert(k);
        root = k;
    }
    else {
        int left = *prev(it);

        if (bit.query(left, k - 1) < a[k]) {
            imp.insert(k);
            root = k;
        }
        else {
            root = left;
        }
    }
    while (true) {
        auto jt = imp.upper_bound(k);

        if (jt == imp.end())
            break;

        int j = *jt;

        if (bit.query(root, j - 1) >= a[j]) {
            imp.erase(j);
        }
        else {
            break;
        }
    }
    ans.push_back(imp.size()-1);
    }
for(int i=n-1;i>-1;i--){
    cout<<ans[i]<<" ";
}
cout<<'\n';
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