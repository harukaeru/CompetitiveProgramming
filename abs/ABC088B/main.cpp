#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

vector<int> input(int N) {
  vector<int> vec(N);
  rep(i, N) {
    cin >> vec.at(i);
  }
  return vec;
}

int main() {
  int N;
  cin >> N;
  vector<int> a = input(N);
  sort(a.begin(), a.end(), greater<int>());

  int alice_sum = 0;
  int bob_sum = 0;

  rep(i, a.size()) {
    if (i % 2 == 0) {
      // alice
      alice_sum += a.at(i);
    } else {
      // bob
      bob_sum += a.at(i);
    }
  }

  cout << alice_sum - bob_sum << endl;

  return 0;
}
