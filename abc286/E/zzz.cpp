#include <chrono>
#include <cmath>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using namespace std::chrono;

const int N2 = 10000000;
int N = sqrt(N2) + 1;

int main() {
  high_resolution_clock::time_point start = high_resolution_clock::now();

  high_resolution_clock::time_point end = high_resolution_clock::now();

  start = high_resolution_clock::now();
  int dp2[N + 1][N + 1];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      dp2[i][j] = 1;
    }
  }
  end = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(end - start);
  cout << duration.count() / 1000 << " ms, list" << endl;

  return 0;
}
