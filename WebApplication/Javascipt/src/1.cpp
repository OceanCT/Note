#include<bits/stdc++.h>
using namespace std;
#define FOUT freopen("out.txt","w",stdout);
int main(){
    FOUT
    for(int i=1;i<=9;i++){
        cout<<"<tr>"<<endl;
        for(int j=1;j<=i;j++){
            cout<<"<td>"<<i<<"*"<<j<<"="<<i*j<<"</td>"<<endl;
        }
        cout<<"</tr>"<<endl;
    }
    return 0;
}