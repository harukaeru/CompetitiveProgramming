#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define reps(i, s, n) for (int i = s; i < (int)(n); i++)

using namespace std;

int sum_of_digits(int num) {
  int sum = 0;
  while (num > 0) {
    sum += num % 10;
    num /= 10;
  }
  return sum;
}

int main() {
  int N;
  int A, B;

  cin >> N;
  cin >> A >> B;

  int total_sum = 0;

  reps(num, 1, N + 1) {
    int digit_sum = sum_of_digits(num);
    if (A <= digit_sum && digit_sum <= B) {
      total_sum += num;
    }
  }

  cout << total_sum << endl;
  return 0;
}