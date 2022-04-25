#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<int> data(5);

  rep(i, 5) {
    cin >> data.at(i);
  }

  rep(i, 4) {
    int current_value = data.at(i);
    int next_value = data.at(i + 1);
    if (current_value == next_value) {
      cout << "YES" << endl;
      return 0;
    }
  }

  cout << "NO" << endl;

  return 0;
}
