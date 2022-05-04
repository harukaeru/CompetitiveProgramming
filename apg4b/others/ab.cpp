#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

struct Kero {
  int a;
  int b;
  int c;

  int add() {
    return a + b;
  }

  Kero(int a_, int b_, int c_) {
    a = a_;
    b = b_;
    c = c_;
    cout << "Called Kero constructor" << endl;
  }

  Kero(const Kero &old_kero) {
    a = old_kero.b;
    b = old_kero.c;
    c = old_kero.a;
  }
};

int main() {
  Kero k2 = {1, 2, 3};

  cout << k2.a << endl;
  cout << k2.b << endl;
  cout << k2.c << endl;
  cout << k2.add() << endl;

  auto k3 = Kero(3, 4, 5);

  cout << k3.c << endl;

  auto k4 = Kero(k3);

  cout << "-------------" << endl;
  cout << k4.a << endl;
  cout << k4.b << endl;
  cout << k4.c << endl;

  Kero k5 = k4;
  cout << "-------------" << endl;
  cout << k5.a << endl;
  cout << k5.b << endl;
  cout << k5.c << endl;
}
