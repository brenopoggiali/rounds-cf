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

ii soma(int n){
	int soma = 0;
	int i=0;
	for (i=1; i<=n; i++){
		soma += i;
		if (soma >= n) break;
	}
	return make_pair(i, soma-i);
}

int main(){ _
	int t; cin >> t;
	int n, k;
	int b1, b2;
	ii som;
	for(int T=0; T<t; T++){
		cin >> n >> k;
		string ans = "";
		som = soma(k);
		b1 = n-1-som.f;
		b2 = n-(k-som.s);
		//cout << k << " " << som.s << " " << b2 << endl;
		for (int N=0; N<n; N++){
			if(N != b1 and N != b2){
				ans += "a";
			}else{
				ans += "b";
			}
		}
		cout << ans << endl;
	}
	
	exit(0);
}
