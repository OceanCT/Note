#include<bits/stdc++.h>
using namespace std;

#define FIN freopen("solution2.txt","r",stdin);
#define FOUT freopen("time2.txt","w",stdout);
#define ENIN freopen("CON","r",stdin);
#define ENOUT freopen("CON", "w", stdout);
#define IOS ios::sync_with_stdio(false);
int main(){
	FIN
	FOUT
	int n = 5;
	while(n--){
		double sum = 0;
		for(int i=1;i<100;i++){
			double tmp;
			cin>>tmp;
			sum+=tmp;
		}
		cout<<to_string(sum/100)<<endl;
	}
	return 0;
}

