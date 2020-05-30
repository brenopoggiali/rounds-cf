#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

#define pb push_back
#define f first
#define s second
#define BUFF ios::sync_with_stdio(false);

typedef long long int ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;

mt19937 rng((int) chrono::steady_clock::now().time_since_epoch().count());

const int MAX = (int)1e5+10;

ll gcd( ll a, ll b ){
	if( b == 0 ) return a;
	return gcd(b, a%b);
}

ll lcm( ll a, ll b, ll c ){
	ll aux = (a*b)/gcd(a,b);
	return (aux*c)/gcd(aux,c);
}

int main(){

    BUFF;

	ll n; cin >> n;

	if( n == 1 ){
		cout << 1 << endl;
		return 0;
	}
	if( n == 2 ){
		cout << 2 << endl;
		return 0;
	}
	if( n == 3 ){
		cout << 6 << endl;
		return 0;
	}

	if( n%2 ){
		cout << n*(n-1)*(n-2) << endl;
		return 0;
	}

	ll mx = 0;
	for( ll i=n; i>=max(n-100, 1ll); i-- ){
		for( ll j=n; j>=max(n-100, 1ll); j-- ){
			for( ll k=n; k>=max(n-100, 1ll); k-- ){
				mx = max(mx, lcm(i, j, k));
			}
		}
	}

	cout << mx << endl;
	
    return 0;
}
