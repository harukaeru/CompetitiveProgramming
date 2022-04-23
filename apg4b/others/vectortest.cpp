#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int N;
  cin >> N;
  vector<int> math(N);
  vector<int> english(N);

  rep(i, N) {
    cin >> math.at(i);
  }

  rep(i, N) {
    cin >> english.at(i);
  }

  rep(i, N) {
    cout << math.at(i) + english.at(i) << endl;
  }
}