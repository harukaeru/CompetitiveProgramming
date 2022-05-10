#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  vector<string> weather = {"Sunny", "Cloudy", "Rainy"};

  auto it = find(weather.begin(), weather.end(), s);
  it++;
  if (it == weather.end()) {
    it = weather.begin();
  }

  cout << *it << endl;

  return 0;
}
