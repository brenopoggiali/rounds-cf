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
	while (T--){
		ll a, b, q; cin >> a >> b >> q;
		ll aux = max(a, b);
		a = min(a, b);
		b = aux;
		vector<int> ans;
		if (a%b == 0 or b%a == 0){
			for (int i=0; i<q; i++){
				int l, r; cin >> l >> r;
				cout << 0 << " ";
			}
			cout << endl;
			continue;
		}
		for (int i=0; i<q; i++){
			ll l, r; cin >> l >> r;
			ll c = 0;
			for (int x=l; x<min(r+1, (ll) a*b); x++){
				if ((x%a)%b != (x%b)%a)	c++;
			}
			ll c2 = 0;
			for (int x=a*b; x<min(r+1, (ll) a*b); x++){
				if ((x%a)%b != (x%b)%a)	c2++;
			}
			c += c2*(r/(a*b));
			for (int x=max(((r/(a*b))*a*b),(ll) a*b*2); x<min(r+1, (ll) a*b); x++){
				if ((x%a)%b != (x%b)%a)	c++;
			}
			ans.pb(c);
		}
		for (auto u : ans){
				cout << u << " ";
			}
			cout << endl;
	}
	
	exit(0);
}
