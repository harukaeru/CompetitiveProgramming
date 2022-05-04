#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)
#include <pprint.hpp>

bool operator<(const pair<int, int> &left, const pair<int, int> &right) {
  if (right.second > left.second) {
    return true;
  }
  return right.first > left.first;
};

int main() {
  vector<pair<int, int>> x = {{3, 2}, {4, 1}, {9, 9}, {2, 32}, {0, 1}, {5, 3}, {0, 7}};

  sort(x.begin(), x.end());
  pprint::PrettyPrinter printer;
  printer.print(x);
}