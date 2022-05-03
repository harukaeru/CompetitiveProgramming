#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)
#include <pprint.hpp>

int main() {
  pair<int, int> p;
  p = make_pair(2, 3);

  tuple<int, string, int> t;
  t = make_tuple(3, "foo", 4);

  int x;
  string y;
  int z;
  int a;
  int b;

  tie(a, b) = p;
  tie(x, y, z) = t;

  cout << a << b << endl;
  cout << x << y << z;
  cout << "-----------" << endl;
  get<2>(t) = 999;
  tie(x, ignore, ignore) = t;
  cout << x;

  cout << "-----------" << endl;
  cout << p.first << p.second << endl;
  auto q = 3.2;
  cout << q << endl;

  cout << "same" << (make_pair(3, 4) == make_pair(3, 4)) << endl;

  vector<tuple<int, int, int>> vec;

  vec.push_back(make_tuple(3, 1, 1));
  vec.push_back(make_tuple(4, 2, 9));
  vec.push_back(make_tuple(1, 3, 5));
  vec.push_back(make_tuple(1, 2, 5));
  vec.push_back(make_tuple(1, 2, 7));

  sort(vec.begin(), vec.end());
  using pp = pprint::PrettyPrinter;
  pp printer;
  printer.print(vec);
}