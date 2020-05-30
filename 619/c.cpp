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

ll sum_to(ll a) {
	return (a*(a+1))/2;
}

int main(){ _
	int t; cin >> t;
	ll total, ones, zeros;
	ll zeros_per_space, rest, spaces;
	ll a, b, ans;
	for (int i=0; i<t; i++) {
		cin >> total >> ones;
		zeros = total-ones;
		spaces = ones+1;

		zeros_per_space = zeros / spaces;
		rest = zeros % spaces;
		
		a = rest * sum_to(zeros_per_space+1) + (spaces-rest) * sum_to(zeros_per_space);

		b = sum_to(total);
		
		ans = b-a;
		
		cout << ans << endl;
	}
	
	exit(0);
}
