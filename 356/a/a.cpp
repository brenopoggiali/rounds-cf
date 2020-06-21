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

bool changed(ii a) {
	return a != make_pair(0, 0);
}

void imprimir(vector<ii> ans){
	for (int i=1; i<ans.size(); i++)
		cout << ans[i].f << " ";
	cout << endl;
}


int main(){
	int n, m; cin >> n >> m;
	vector<ii> ans(n+1, make_pair(0, 0));
	for (int __=0; __<m; __++) {
		int l, r, x; cin>> l >> r >> x;
		int i; i = l;
		while (i <= r) {
			imprimir(ans);
			if (changed(ans[i])){
				if (r >= ans[i].f and x != ans[i].f and !changed(ans[ans[i].f])){
					ans[ans[i].f] = make_pair(x, ans[i].s+1);
				}
				i = ans[i].s;
				if (changed(ans[i])) ans[i].s = r;
			}
			else if (i != x) {
				ans[i] = make_pair(x, r);
			}
			i++;
		}
	}
	imprimir(ans);
	
	exit(0);
}
