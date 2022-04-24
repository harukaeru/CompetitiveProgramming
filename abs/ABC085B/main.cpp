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

int VALUE_CONSTRAINT = 100;

int main() {
  int N;
  cin >> N;

  vector<int> d_vec = input(N);
  set<int> values;

  rep(i, d_vec.size()) {
    values.insert(d_vec.at(i));
  }

  cout << values.size() << endl;
}
