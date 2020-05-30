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
	int t; cin >> t;
	while (t--){
		int n; cin >> n;
		vector<int> a;
		int aux;
		for (int i=0; i<n; i++){
			cin >> aux;
			a.pb(aux);
		}
		vector<vector<int>> alph(26, vector<int>(n, 0));
		for (int i=0; i < n; i++){
			if (i == 0){
				for (int c=0; c<26; c++){
					if (c+1 == a[i]) alph[c][i] = 1;
				}
			}
			else{
				for (int c=0; c<26; c++){
					alph[c][i] = alph[c][i-1];
					if (c+1 == a[i]) alph[c][i]++;
				}
			}
		}
		int maxi = 0;
		for(int i=0; i < 26; i++){
			if (alph[i][n-1] == 0) continue;
			for (int j=0; j < 26; j++){
				if (i == j) maxi = max(maxi, alph[i][n-1]);
				else if (alph[j][n-1] == 0) continue;
				else {
					for (int k=0; k<n; k++){
						int x = alph[i][k];
						for (int l=k+1; l<n-1; l++){
							int x2 = alph[i][n-1]-alph[i][l];
							int y = alph[j][l]-alph[j][k];
							maxi = max(maxi, (2*min(x2, x)+ y));
						}
					}
				}
			}
		}
		cout << maxi << endl;
	}
	
	exit(0);
}
