#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int> scores(N);

  int sum = 0;
  rep(i, N) {
    cin >> scores.at(i);
    sum += scores.at(i);
  }

  int avg = sum / N;

  rep(i, N) {
    int distance = avg - scores.at(i);
    if (distance < 0) {
      distance = distance * (-1);
    }
    cout << distance << endl;
  }

  return 0;
}
