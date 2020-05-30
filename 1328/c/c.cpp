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
	int T; cin >> T;
	int N;
	for (int t=0; t<T; t++){
		cin >> N;
		string s;
		cin >> s;
		string ans1 = "1";
		string ans2 = "1";
		bool start = false;
		for (int n=1; n<N; n++){
			if (!start){
				if (s[n] == '1'){
					start = true;
					ans1 += '1';
					ans2 += '0';
				}
				else {
					if (s[n] == '2'){
						ans1 += '1';
						ans2 += '1';
					}
					else{
						ans1 += s[n];
						ans2 += s[n];
					}
				}
			}
			else {
				ans1 += '0';
				ans2 += s[n];	
			}
		}
		cout << ans1 << endl;
		cout << ans2 << endl;
	}
	exit(0);
}
