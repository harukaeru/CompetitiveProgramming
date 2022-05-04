#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

struct MyPair {
  int x;
  string y;

  MyPair operator+(const MyPair &other) {
    MyPair ret;
    ret.x = x + other.x;
    ret.y = y + other.y;
    return ret;
  }

  void operator=(const MyPair &other) {
    cout << "= was called" << endl;
    x = other.y.size();
    y = to_string(other.x);
  }
};

int main() {
  MyPair p1 = {1, "foo"};
  MyPair p2 = {2, "bar"};

  MyPair p3 = p1 + p2;

  cout << p3.x << " " << p3.y << endl;

  MyPair p4;
  p4 = p3;
  cout << p4.x << " " << p4.y << endl;
}