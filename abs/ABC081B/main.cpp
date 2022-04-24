#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

vector<int> input(int N) {
  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }
  return vec;
}

int main() {

  int N;
  cin >> N;

  vector<int> vec = input(N);

  int divided_number = 0;

  while (true) {
    rep(i, N) {
      if (vec.at(i) % 2 != 0) {
        cout << divided_number << endl;
        return 0;
      } else {
        vec.at(i) /= 2;
      }
    }
    divided_number++;
  }
}
