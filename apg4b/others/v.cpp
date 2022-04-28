#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int sum_range(int a, int b) {
  if (a >= b) {
    return b;
  }

  return a + sum_range(a + 1, b);
}

int array_sum(vector<int> &arr) {
  if (arr.size() == 0) {
    return 0;
  }
  int last_int = arr.at(arr.size() - 1);

  arr.pop_back();

  return last_int + array_sum(arr);
}

bool has_divider(int n, int v) {
  if (n == v) {
    return false;
  }

  if (n % v == 0) {
    return true;
  }

  return has_divider(n, v + 1);
}

bool is_prime(int n) {
  if (n <= 0) {
    return false;
  }
  if (n <= 2) {
    return true;
  }

  return !has_divider(n, 2);
}

void reverse_array(vector<int> &vec) {
  cout << "test" << endl;
  for (int i = 0; i < (int)(vec.size()) / 2; i++) {
    int temp = vec.at(i);
    vec.at(i) = vec.at((vec.size() - 1) - i);
    vec.at((vec.size() - 1) - i) = temp;
  }
}

int main() {
  cout << sum_range(0, 10) << endl;
  cout << sum_range(1, 10) << endl;
  cout << sum_range(1, 3) << endl;
  cout << sum_range(2, 3) << endl;
  cout << "-------------------" << endl;
  vector<int> a = {1, 2, 3, 4, 5};
  vector<int> b = {3, 8, 9, 10, 20, 55};
  // cout << array_sum(a) << endl;
  // cout << array_sum(b) << endl;
  cout << "-------------------" << endl;
  cout << is_prime(2) << endl;
  cout << is_prime(3) << endl;
  cout << is_prime(4) << endl;
  cout << is_prime(19) << endl;
  cout << is_prime(31) << endl;
  cout << is_prime(35) << endl;
  cout << "-------------------" << endl;
  cout << "a.size" << a.size() << endl;
  reverse_array(a);
  reverse_array(b);
  cout << "a.size" << a.size() << endl;
  rep(i, a.size()) {
    cout << a.at(i) << " ";
  }
  cout << endl;
  rep(i, b.size()) {
    cout << b.at(i) << " ";
  }
}