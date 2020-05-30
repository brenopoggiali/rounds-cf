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

bool is_palindrome(string s1, int begin, int end){
	cout << s1 << " " << begin << " " << end << endl;
	for (int i=begin; i<end; i++){
		if (s1[i] != s1[s1.size()-i-1])
			//cout << s1 << " " << begin << " " << end << endl;
			return false;
	}
	//cout << "TRYE " << s1 << " " << begin << " " << end << endl;
	return true;
}

string get_max_palindrome(string s, int begin, int end) {
	string pal = "";
	for (int i=end; i<begin; i--){
		if (is_palindrome(s, begin, i)){
			for (int j=begin; j<i; j++){
				pal += s[j];
			}
			break;
		}
	}
	return pal;
}
string get_max_palindrome_final(string s, int begin, int end) {
	string pal = "";
	cout << "R - " << begin << " " << end << endl;
	for (int i=begin; i<end; i++){
		cout << is_palindrome(s, i, end) << endl;
		if (is_palindrome(s, i, end)){
			cout << "ENTROU" << endl;
			for (int j=i; j<end; j++){
				pal += s[j];
			}
			break;
		}
	}
	return pal;
}

int main(){ _
	int n; cin >> n;
	string s, pre, suf, pre2, suf2;
	int i;
	for (int t=0; t<n; t++){
		cin >> s;
		pre = ""; suf = "";
		i = 0;
		while (i != s.size()-1-i and s[i] == s[s.size()-1-i]){
			pre += s[i];
			suf += s[s.size()-1-i];
			i++;
		}
		pre2 = get_max_palindrome(s, i, s.size()-suf.size());
		suf2 = get_max_palindrome_final(s, pre.size(), s.size()-suf.size());
		cout << "suf2 " << suf2 << endl;
		if (pre2.size() < suf2.size()){
			suf += suf2;
		}
		else {
			pre += pre2;
		}

		reverse(suf.begin(), suf.end());
		cout << pre + suf << endl;
	}
	
	exit(0);
}
