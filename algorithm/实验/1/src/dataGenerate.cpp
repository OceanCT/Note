#include<bits/stdc++.h>
using namespace std;

#define IN freopen("in.txt","r",stdin);
#define OUT freopen("data.txt","w",stdout);
#define ENIN freopen("CON","r",stdin);
#define ENOUT freopen("CON", "w", stdout);
#define IOS ios::sync_with_stdio(false);

void generate_data(int n){
	for(int i=1;i<=100;i++){
		cout<<n<<endl;
		for(int i = 1;i<=n;i++){
			cout<<rand()<<" ";
		}	
		cout<<endl;	
	}
} 
int main(){
	OUT
	IOS
	srand(time(NULL));
	int t = 500;
	cout<<t<<endl;
	int n = 10;
	generate_data(n);
	n = 100;
	generate_data(n);
	n = 1000;
	generate_data(n);
	n = 10000;
	generate_data(n);
	n = 100000;
	generate_data(n);
	return 0;
}

