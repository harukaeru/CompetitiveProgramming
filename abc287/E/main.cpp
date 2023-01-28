#include <bits/stdc++.h>
#include <iostream>
#include <set>
#include <unordered_map>
using namespace std;

class Node {
  public:
  char x;
  set<int> s;
  unordered_map<char, Node *> children;

  Node(char x, int v) : x(x) {
    s.insert(v);
  }
};

int main() {
  int N;
  cin >> N;
  vector<string> S;
  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    S.push_back(s);
  }

  Node *root = new Node(0, 0);
  for (int v = 0; v < N; v++) {
    Node *check_node = root;
    string s = S[v];
    for (int i = 0; i < (int)s.size(); i++) {
      char c = s[i];
      auto child_node = check_node->children.find(c);
      if (child_node != check_node->children.end()) {
        child_node->second->s.insert(v);
        check_node = child_node->second;
        continue;
      }
      Node *new_node = new Node(c, v);
      check_node->children[c] = new_node;
      check_node = new_node;
    }
  }

  for (int v = 0; v < N; v++) {
    string s = S[v];
    Node *check_node = root;
    int cnt = 0;
    set<int> ss = {v};

    for (int i = 0; i < (int)s.size(); i++) {
      auto nex = check_node->children[s[i]];
      std::set<int> diff;

      set_difference(nex->s.begin(), nex->s.end(), ss.begin(), ss.end(), std::inserter(diff, diff.begin()));
      if (diff.size() > 0) {
        cnt++;
        check_node = nex;
      } else {
        break;
      }
    }
    cout << cnt << endl;
  }

  return 0;
}