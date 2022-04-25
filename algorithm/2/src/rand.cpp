#include<bits/stdc++.h>
using namespace std;
#define FOUT freopen("test","w",stdout);
void generate(int n,int m){
    cout<<n<<" "<<m<<endl;
    for(int i=1;i<=n;i++){
        cout<<rand()%10<<" ";
    }
    cout<<endl;
    for(int i=1;i<=m;i++){
        cout<<rand()%10<<" ";
    }
    cout<<endl;
    cout<<endl;
}
int main(){
    FOUT
    srand(time(NULL));
    for(int i=10;i<=10000;){
        int k = 10;
        while(k--){
            generate(i,i);
        }
        i*=10;
    }
    return 0;
}