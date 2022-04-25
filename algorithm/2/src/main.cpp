#include<bits/stdc++.h>
using namespace std;
#define FIN freopen("test","r",stdin);
#define FOUT freopen("main1Res","w",stdout);
#define N 10005
int n,m;
int a[N];
int b[N];
int f[N][N];
int last[N];
void read(){
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	for(int i=1;i<=m;i++){
		cin>>b[i];
	}
}

int main(){	
	FIN
	FOUT
	read();
	for(int i=1;i<=n;i++){
		int tmp = 0;
		int t = 0;
		for(int j=1;j<=m;j++){
			f[i][j] = f[i-1][j];
			if(a[i]==b[j]){
				if(tmp+1>f[i][j]){
					f[i][j] = tmp+1;
					last[j] = t;
				}
			} 
			if(b[j]<a[i]){
				if(f[i-1][j]>tmp){
					tmp = f[i-1][j];
					t = j;
				}
			} 
		}
	}	
	int ans = 0;
	int last1 = 0;
	for(int j=1;j<=m;j++){
		if(f[n][j]>ans){
			ans = f[n][j];
			last1 = j;
		}
	}
	cout<<ans<<endl;
	stack<int> sk;
	while(last1){
		sk.push(b[last1]);
		last1 = last[last1];
	}
	while(!sk.empty()){cout<<sk.top()<<" ";sk.pop();}	
	cout<<endl;
	return 0;
}