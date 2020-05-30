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

string s;

ll go( char a, char b ){
	ll ret=0;
	ll at=0;

	for( char c : s ){
		if( c == b ){
			ret += at;
		}
		if( c == a ){
			at++;
		}
	}

	return ret;
}

int main(){

    BUFF;

	cin >> s;

	ll mx = 0;
	map<char, ll> m;

	for( char c : s ){
		m[c]++;
	}

	for( auto e : m ){
		mx = max(mx, e.s);
	}

	for( int i='a'; i<='z'; i++ ){
		for( int j='a'; j<='z'; j++ ){
			mx = max(mx, go((char)i, (char)j));
		}
	}

	cout << mx << endl;


    return 0;
}
