#include<bits/stdc++.h>
using namespace std;
#define TEST1 freopen("mainRes","r",stdin);
#define TEST2 freopen("main1Res","r",stdin);
vector<string> vec1,vec2;
int main(){
	string str;
	TEST1
	while(cin>>str){
		vec1.push_back(str);
	}
	cin.clear();
	TEST2
	while(cin>>str){
		vec2.push_back(str);
	}
	int len = vec1.size();
	bool flag = true;
	for(int k=0;k<len;k++){if(vec1[k]!=vec2[k]) flag = false;}
	if(flag){
		cout<<"YES"<<endl;
	}
	else cout<<"NO"<<endl;

	return 0;
}