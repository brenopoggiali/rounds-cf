#include <bits/stdc++.h>
 
using namespace std;
 
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define f first
#define s second
#define pb push_back
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
 
int main(){ _
	int T; cin >> T;
	int K, aux;
	for (int t=0; t<T; t++){
		int N; cin >> N;
		set<int> kings;
		set<int> princess;
		for (int n=1; n<=N; n++){
			kings.insert(n);
			princess.insert(n);
		}
		for (int n=1; n<=N; n++){
			cin >> K;
			bool flag = true;
			for (int k=0; k<K; k++){
				cin >> aux;
				if (flag and kings.count(aux)){
					kings.erase(aux);
					princess.erase(n);
					flag = false;
				}
			}
		}
		int kin, prin; 
		for (auto la : kings){
			kin = la;
			break;
		}
		for (auto la : princess){
			prin = la;
			break;
		}
		if (kings.size() and princess.size()){
			cout << "IMPROVE" << endl;
			cout << prin << " " << kin << endl;
		}
		else {
			cout << "OPTIMAL" << endl; 
		}
	}	
	exit(0);
}
