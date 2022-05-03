#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  vector<pair<int, int>> p_list;

  rep(i, N) {
    pair<int, int> a;
    cin >> a.second >> a.first;
    p_list.push_back(a);
  }

  sort(p_list.begin(), p_list.end());

  rep(i, N) {
    int a, b;
    tie(b, a) = p_list.at(i);
    cout << a << " " << b << endl;
  }

  return 0;
}
