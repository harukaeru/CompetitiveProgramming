#include <bits/stdc++.h>
#include <pprint.hpp>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

/*
int square(int x) {
  return x * x;
}

double square(double x) {
  return x * x;
}
*/

template <typename T>
T square(T x) {
  return x * x;
}

template <int INDEX1, int INDEX2>
void swap_index(tuple<int, int, int> &t) {
  swap(get<INDEX1>(t), get<INDEX2>(t));
}

int main() {

  tuple<int, int, int> t = make_tuple(1, 2, 3);
  swap_index<0, 1>(t);

  pprint::PrettyPrinter printer;
  printer.print(t);
  cout << square(3) << endl;
  cout << square(3.14) << endl;
}