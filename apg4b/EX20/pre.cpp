#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

#include <pprint.hpp>
#include <vector>

int main() {
  vector<int> x = {1, 2, 3, 4, 5, 40, 999, 3020};
  vector<int> x2 = {13, 48, 89, 7, 100, 1, 4};
  vector<vector<int>> y = {};

  rep(i, 10) {
    y.push_back(x);
    y.push_back(x2);
  }
  pprint::PrettyPrinter printer;

  printer.print(x);
  cout << "-----------------" << endl;
  printer.print(y);

  return 0;
}
