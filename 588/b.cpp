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
	int n, k;
	cin >> n >> k;
	string s;
	cin >> s;
	int k_aux = 0;
	int i = 0;
	if (i == 0 and k >0) {
		if (s[i] == '1')
			i++;
		else {
			s[i] = '1';
			k_aux++;
			i++;
		}
	}
	while (i < n and k_aux < k){
		if (s[i] == '0')
			i++;
		else {
			s[i] = '0';
			k_aux++;
			i++;
		}
	}

	if (n==1 and k >0)
		cout << 0 << endl;
	else
		cout << s << endl;

	exit(0);
}
