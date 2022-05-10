#include<bits/stdc++.h>
#include<windows.h>
using namespace std;
#define FIN freopen("data.txt","r",stdin);
#define FOUT freopen("solution2.txt","w",stdout);
#define ENIN freopen("CON","r",stdin);
#define ENOUT freopen("CON", "w", stdout);
#define IOS ios::sync_with_stdio(false);
#define N 100005
int t;
int n;
int a[N];
int b[N];
long long cnt;
void inita(){
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
}
void merge(int l,int r){
	// cout<<l<<" "<<r<<endl;
	// 1 2 3 3
	if(l==r) return;
	int mid = (l+r)/2;
	merge(l,mid);
	merge(mid+1,r);
	int p1 = l;
	int p2 = mid+1;
	int now = l;
	int cnt1 = 0;
	while(p1<=mid&&p2<=r){
		if(a[p1]>a[p2]){
 			b[now++] = a[p2++];
			cnt1++;
		}else{
			b[now++] = a[p1++];
			cnt+=cnt1;
		}
	}
	while(p2<=r){
		b[now++] = a[p2++];		
	}
	while(p1<=mid){
		b[now++] = a[p1++];
		cnt+=cnt1; 
	}
	for(int i=l;i<=r;i++) a[i] = b[i];
	// cout<<l<<" "<<r<<" "<<cnt<<endl;
}
int main(){
	FIN
	FOUT
	IOS
	cin>>t;
	for(int i=1;i<=t;i++){
		cnt = 0;
		DWORD start = GetTickCount();
		inita();
		merge(1,n);	
		// cout<<cnt<<endl; 
		DWORD end = GetTickCount();
		cout<<end-start<<endl;
	}
	return 0;
}

