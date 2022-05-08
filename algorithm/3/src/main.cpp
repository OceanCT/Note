#include<bits/stdc++.h>
using namespace std;
#define N 200005
typedef struct Node{
    int l,u;
    int pos;
    const bool operator<(Node other)const{
        if(l!=other.l){
            return l<other.l;
        }
        else{
            return u>other.u;
        }
    }
}node;
vector<node> g;
bool flag[N];
int main(){
    cin>>n;
    priority_queue<node> q;
    for(int i=1;i<=n;i++){
        int a,b;
        cin>>a>>b;
        g.push_back({a,b,i});
        q.push({a,b,i});
    }
    int en = 0;
    int tmp = 0;
    while(!q.empty()){
        node now = q.top();
        q.pop();
        if(now.l>en){
            flag[tmp.pos] = true;
            en = tmp.b;
            q.push(now);
        }else if(now.r<=en){

        }else if(now.r>tmp.r){
            tmp = now;
        }
    }
    for(int i=1;i<+n;i++){
        if(flag[i]){
            cout<<"("<<g.a<<","<<g.b<<"),";
        }
    }
    cout<<endl;
    return 0;
}