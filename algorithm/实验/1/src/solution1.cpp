#include<bits/stdc++.h>
using namespace std;
#define FIN freopen("data.txt","r",stdin);
#define FOUT freopen("solution1.txt","w",stdout);
#define ENIN freopen("CON","r",stdin);
#define ENOUT freopen("CON", "w", stdout);
#define IOS ios::sync_with_stdio(false);
#define N 100005
int t;
int n;
int a[N];
void inita(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];	
}
void solve(){
	inita();
	long long cnt = 0;
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			if(a[i]>a[j]) cnt++;
		}
	// cout<<cnt<<endl;
	}
}
int main(){
	FIN
	FOUT
	// IOS
	cin>>t;
	// t = 1;
	for(int i=1;i<=t;i++){
		auto start = chrono::high_resolution_clock::now();
		solve();		
		auto end = chrono::high_resolution_clock::now();
		auto diff = end-start;
		cout<<diff.count()<<endl;
		cerr<<"Finished "<<i<<endl;
	}
	return 0;
}

