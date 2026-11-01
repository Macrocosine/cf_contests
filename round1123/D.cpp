#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve() {
    int n;
    cin>>n;
    vector<int>a(n);
    for(int&x:a)cin>>x;
    vector<int>q(n+1);
    for(int i=0;i<n;i++){
        if (i%2)q[a[i]]=1;
        else q[a[i]]=0;
    }
    int balance=0;
    for(int x=n;x>0;x--){
        if(q[x]==1)balance++;
        else balance--;
        if(abs(balance)>1){
            cout<<"No"<<endl;
            return;
        }
    }
    cout<<"Yes"<<endl;
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