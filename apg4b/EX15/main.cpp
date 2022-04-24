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

int sum(vector<int> vec) {
  int result = 0;
  rep(i, vec.size()) {
    result += vec.at(i);
  }
  return result;
}

int main() {
  int N;
  cin >> N;

  vector<int> A = input(N);
  vector<int> B = input(N);
  vector<int> C = input(N);

  cout << sum(A) * sum(B) * sum(C) << endl;

  return 0;
}
