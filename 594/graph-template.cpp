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

void addEdge(vector <vector <int>> &g, int a, int b, bool both=false) {
	g[a].push_back(b);
	if (both) 
		g[b].push_back(a);
}


void printGraph(vector <vector<int>> g, int V)
{
    for (int v = 0; v < V; ++v)
    {
        cout << "\n Adjacency list of vertex "
             << v << "\n head ";
        for (auto x : g[v])
           cout << "-> " << x;
        printf("\n");
    }
}

int main(){ _
	int n, m; cin >> n >> m;
	vector <vector <int>> g(n+1);
	
	int a,b;
	for (int i = 0; i < m; ++i) {
		cin >> a >> b;
		addEdge(g, a, b, true);
	}
	
	printGraph(g, n);
	exit(0);
}
