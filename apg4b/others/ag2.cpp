#include <bits/stdc++.h>
#include <pprint.hpp>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

template <typename T>
T square(T x) {
  return x * x;
}

int main() {

  vector<int> a = {3, 2, 8, 5, 4, 7, 13};

  auto it = a.begin();
  vector<int>::iterator it2 = it + 4;

  sort(a.begin() + 2, a.end());

  auto l_it = lower_bound(a.begin(), a.end(), 4);
  auto u_it = upper_bound(a.begin(), a.end(), 4);

  cout << "*l_it: " << *l_it << endl;
  cout << "*u_it: " << *u_it << endl;

  cout << *it2 << endl;

  pprint::PrettyPrinter printer;
  printer.print(a);

  cout << square(3) << endl;
  cout << square(3.14) << endl;
}