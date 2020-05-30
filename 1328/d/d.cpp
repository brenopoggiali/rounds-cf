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
	int T, t;
	int Q; cin >> Q;
	int N;
	for(int q=0; q<Q; q++){
		cin >> N;
		vector<int> ans;
		vector<int> animals;
		for (int n=0; n<N; n++){
			cin >> t;
			animals.pb(t);
		}
		int color = 1;
		int count = 1;
		ans.pb(1);
		if (N%2 == 0){
			bool all_same = true;
			for (int n=1; n<N; n++){
				if (animals[n] != animals[n-1]){
					all_same = false;
					break;
				}
			}
			if (all_same){
				for (int n=1; n<N; n++){
					ans.pb(1);
				}
			}
			else {
				count++;
				for (int n=1; n<N; n++){
					if(all_same) ans.pb(1);
					else ans.pb(2);
					all_same = !all_same;
				}
			}
		}
		else {
			bool jose = true;
			bool all_same = true;
			for (int n=1; n<N; n++){
				if (animals[n] != animals[n-1]){
					all_same = false;
					break;
				}
			}
			if (all_same){
				for (int n=1; n<N; n++){
					ans.pb(1);
				}
			}
			else{
				for (int n=1; n<N; n++){
					if (jose and animals[n] == animals[n-1]){
						ans.pb(ans[n-1]);
						jose = false;
					}
					else {
						if (count == 1) count++;
						if (color == 1) color = 2;
						else color = 1;
						ans.pb(color);
					}
				}
			}
			if (ans[ans.size()-1] == ans[0] and animals[0] != animals[animals.size()-1]){
				count++;
				ans[ans.size()-1] = 3;
			}
		}
		cout << count << endl;
		for(auto i : ans){
			cout << i << " ";
		}
		cout << endl;
	}
	
	exit(0);
}
