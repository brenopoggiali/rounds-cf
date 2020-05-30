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
	int n; cin >> n;
	vector<int> first_color();first_color.push_back(0);
	vector<int> sec_color();sec_color.push_back(0);
	vector<int> third_color();third_color.push_back(0);
	vector <vector <int>> g(n+1);
	int cost;
	for (int i=0; i < n; ++i) {
		cin >> cost;
		first_color.push_back(cost);
	}
	for (int i=0; i < n; ++i) {
		cin >> cost;
		sec_color.push_back(cost);
	}
	for (int i=0; i < n; ++i) {
		cin >> cost;
		third_color.push_back(cost);
	}
	int a,b;
	for (int i = 0; i < n-1; ++i) {
		cin >> a >> b;
		addEdge(g, a, b, true);
	}
	
	printGraph(g, n);
	exit(0);
}
