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

const int LOG = (int)32;
const int MAX = (int)1e5+10;

int n, t=0;
int in[MAX], out[MAX];
int dp[MAX][LOG];
vector<int> g[MAX];
int dist[MAX];

void dfs( int u, int p, int d ){
  in[u] = t++;
  dist[u] = d;
  for( int e : g[u] ) if( e != p ){
    dp[e][0] = u;
    dfs(e, u, d+1);
  }
  out[u] = t;
}

void build(){
  for( int i=0; i<n; i++ ){
    dp[i][0] = i;
  }
  t = 0;
  dfs(0, 0, 0);
  for( int k=1; k<LOG; k++ ){
    for( int i=0; i<n; i++ ){
      dp[i][k] = dp[dp[i][k-1]][k-1];
    }
  }
}

bool anc( int p, int f ){
  return in[p] <= in[f] and out[f] <= out[p];
}

int lca( int u, int v ){
  if( anc(u, v) ){
    return u;
  }
  if( anc(v, u) ){
    return v;
  }
  for( int k=LOG-1; ~k; k-- ){
    if( !anc(dp[u][k], v) ){
      u = dp[u][k];
    }
  }
  return dp[u][0];
}

int get_d(int a, int b){
	return dist[a]+dist[b] - 2*dist[lca(a, b)];
}

bool show( int d, int k ){
	return d<=k and d%2 == k%2;
}

int main(){

    BUFF;

	cin >> n;

	for( int i=0; i<n-1; i++ ){
		int a, b; cin >> a >> b; a--, b--;
		g[a].pb(b);
		g[b].pb(a);
	}

	build();

	int q; cin >> q;

	while( q-- ){
		int x, y, a, b, k; 

		cin >> x >> y; x--, y--;
		cin >> a >> b; a--, b--;
		cin >> k;

		bool ok = show(get_d(a, b), k);
		ok = ok or show(get_d(a, x)+1+get_d(y, b), k);
		ok = ok or show(get_d(a, y)+1+get_d(x, b), k);

		if( ok ){
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}


    return 0;
}
