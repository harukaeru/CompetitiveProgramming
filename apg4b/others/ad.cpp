#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

#include <pprint.hpp>

int main() {
  cout << (int)'A' << endl;

  for (int i = 0; i <= ('Z' - 'A'); i++) {
    cout << (char)tolower('A' + i);
  }

  char c = 'X';
  if ('A' <= c && c <= 'Z') {
    cout << "UPPER" << endl;
  } else {
    cout << "LOWER" << endl;
  }

  auto my_min = [&](int a, int b) {
    return (char)(c + (a < b ? a : b));
  };

  cout << my_min(3, 9) << endl;
  cout << my_min(13, 9) << endl;

  function<int(int)> sum = [&](int n) {
    if (n == 0) {
      return 0;
    }

    return n + sum(n - 1);
  };

  cout << "sum(10): " << sum(10) << endl;

  vector<int> xxx = {1, 2, 3, 4, 9, 2, 3};

  sort(xxx.begin(), xxx.end(), [](int x, int y) { return x > y; });

  pprint::PrettyPrinter printer;
  printer.print(xxx);
}