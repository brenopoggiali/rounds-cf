#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define endl '\n'
#define f first
#define pb push_back

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;

int main(){ _
	int q; cin >> q;
	
	for (int l=0; l<q; l++) {
		long long n, k; cin >> n >> k;
		string s; cin >> s;
		deque <int> zeros;
		map<int, int> zeros2;
		for (int i=0; i<n; i++) {
			if (s[i] == '0')
				zeros.push_back(i);
		}
		int sm;
		if (zeros.size() > 0)
			sm = zeros[0];
		else
			sm = k+1;
		int count = 0;
		while(sm-count <= k) {
			zeros.pop_front();
			k -= sm-count;
			count++;
			if (zeros.size() >0)
				sm = zeros[0];
			else
				break;
		}
		if (zeros.size() and k>0) {
			zeros.pop_front();
			sm -= k;
		}
		else
			sm = n+1;
		string ans = "";
		for (int i = 0; i<zeros.size(); i++) {
			zeros2[zeros[i]] = 0;
		}
		for (int i = 0; i<n; i++) {
			if (i >= count and !zeros2.count(i) and i!=sm)
				ans += '1';
			else
				ans += '0';
		}
		cout << ans << endl;

	}
	
	exit(0);
}
