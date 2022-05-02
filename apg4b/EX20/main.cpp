#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;
#include <algorithm>
#define FMT_HEADER_ONLY
#include <fmt/ranges.h>

#include <iterator>
#include <vector>

int count_report_num(vector<vector<int>> &children_list, int x) {
  vector<int> children = children_list.at(x);

  int sum_of_report = 1;
  rep(i, children.size()) {
    int child = children.at(i);
    sum_of_report += count_report_num(children_list, child);
  }
  return sum_of_report;
}

int main() {
  int N;
  cin >> N;

  vector<int> p(N);
  vector<vector<int>> children_list(N);
  for (int i = 1; i <= N - 1; i++) {
    cin >> p.at(i);
    children_list.at(p.at(i)).push_back(i);
  }

  vector<int> x = {1, 2, 3, 4, 5};
  vector<vector<int>> y = {
      x,
      x};

  fmt::print("{}", y);

  rep(i, N) {
    cout << count_report_num(children_list, i) << endl;
  }

  return 0;
}
