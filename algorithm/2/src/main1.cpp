#include<bits/stdc++.h>
using namespace std;
#define FIN freopen("test","r",stdin);
#define FOUT freopen("main1Res","w",stdout);
#define N 10005
int n,m;
int a[N];
int b[N];
int f[2][N];
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
	int now = 0;
	for(int i=1;i<=n;i++){
		int next = now & 1;
		int tmp = 0;
		int t = 0;
		for(int j=1;j<=m;j++){
			f[next][j] = f[now][j];
			if(a[i]==b[j]){
				if(tmp+1>f[next][j]){
					f[next][j] = tmp+1;
					last[j] = t;
				}
			} 
			if(b[j]<a[i]){
				if(f[now][j]>tmp){
					tmp = f[now][j];
					t = j;
				}
			} 
		}
		now = next;
	}	
	int ans = 0;
	int last1 = 0;
	for(int j=1;j<=m;j++){
		if(max(f[0][j],f[1][j])>ans){
			ans = max(f[0][j],f[1][j]);
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