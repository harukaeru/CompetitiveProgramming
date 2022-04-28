#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int complete_time(vector<vector<int>> children_list, int target) {
  vector<int> children = children_list.at(target);
  if (children.size() == 0) {
    return 0;
  }

  int max_complete_time = 0;
  rep(i, children.size()) {
    max_complete_time = max(max_complete_time, complete_time(children_list, children.at(i)));
  }

  return 1 + max_complete_time;
}

int main() {
  int N;
  cin >> N;

  vector<int> p(N);
  p.at(0) = -1;
  for (int i = 1; i < N; i++) {
    cin >> p.at(i);
  }

  vector<vector<int>> children_list(N);
  for (int i = 1; i < N; i++) {
    int parent = p.at(i);
    children_list.at(parent).push_back(i);
  }

  cout << complete_time(children_list, 0) << endl;
}