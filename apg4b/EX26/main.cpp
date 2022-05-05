#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

map<string, int> int_memo;
map<string, vector<int>> vector_memo;

struct Token {
  string type;
  string value;
};

int execute_int_expression(vector<Token> &tokens) {
  int value = 0;
  string op = "+";

  for (auto token : tokens) {
    if (token.type == "digit") {
      if (op == "+") {
        value += stoi(token.value);
      } else if (op == "-") {
        value -= stoi(token.value);
      }
      op = "";
    } else if (token.type == "op_add") {
      op = "+";
    } else if (token.type == "op_subtract") {
      op = "-";
    } else if (token.type == "variable") {
      int target = int_memo[token.value];
      if (op == "+") {
        value += target;
      } else if (op == "-") {
        value -= target;
      }
      op = "";
    }
  }

  return value;
}

vector<int> add_vectors(vector<int> &x, vector<int> &y) {
  rep(i, x.size()) {
    x.at(i) += y.at(i);
  }
  return x;
}

vector<int> subtract_vectors(vector<int> &x, vector<int> &y) {
  rep(i, x.size()) {
    x.at(i) -= y.at(i);
  }
  return x;
}

vector<int> execute_vector_expression(vector<Token> &tokens) {
  vector<int> initial;

  string op = "+";

  for (int i = 0; i < (int)tokens.size(); i++) {
    Token token = tokens.at(i);
    if (token.type == "open_bracket") {
      vector<int> a;
      while (token.type != "close_bracket") {
        i++;
        token = tokens.at(i);
        if (token.type == "close_bracket") {
          break;
        }
        vector<Token> int_unit = {token};
        int value = execute_int_expression(int_unit);
        a.push_back(value);
      }

      if (initial.empty()) {
        initial = a;
      } else {
        if (op == "+") {
          initial = add_vectors(initial, a);
        } else if (op == "-") {
          initial = subtract_vectors(initial, a);
        }
      }
      op = "";
    } else if (token.type == "op_add") {
      op = "+";
    } else if (token.type == "op_subtract") {
      op = "-";
    } else if (token.type == "variable") {
      vector<int> a = vector_memo[token.value];

      if (initial.empty()) {
        initial = a;
      } else {
        if (op == "+") {
          initial = add_vectors(initial, a);
        } else if (op == "-") {
          initial = subtract_vectors(initial, a);
        }
      }
      op = "";
    }
  }

  return initial;
}

/*
int execute_int_statement() {
}
*/

int main() {
  int N;
  cin >> N;

  vector<vector<Token>> commands;
  rep(i, N) {
    vector<Token> vec;
    string t;
    while (t != ";") {
      Token tok;
      cin >> t;

      if (t == "int" || t == "print_int" || t == "print_vec" || t == "vec") {
        tok.type = t;
        tok.value = t;
      }

      for (char c = '1'; c <= '9'; c++) {
        string s = "";
        s += c;
        if (t == s || t == ("-" + s)) {
          tok.type = "digit";
          tok.value = t;
        }
      }

      for (char c = 'a'; c <= 'z'; c++) {
        string s = "";
        s += c;
        if (t == s) {
          tok.type = "variable";
          tok.value = t;
        }
      }

      if (t == "+") {
        tok.type = "op_add";
        tok.value = "+";
      } else if (t == "-") {
        tok.type = "op_subtract";
        tok.value = "-";
      } else if (t == "=" || t == ",") {
        continue;
      }

      if (t == "[") {
        tok.type = "open_bracket";
        tok.value = "[";
      } else if (t == "]") {
        tok.type = "close_bracket";
        tok.value = "]";
      }

      if (t == ";") {
        break;
      }

      vec.push_back(tok);
    }
    commands.push_back(vec);
  }

  rep(i, N) {
    auto cmd = commands.at(i);
    auto c = cmd.at(0);
    if (c.type == "int") {
      Token variable = cmd.at(1);

      vector<Token> sliced = vector<Token>(cmd.begin() + 2, cmd.end());
      int value = execute_int_expression(sliced);

      int_memo[variable.value] = value;
    } else if (c.type == "print_int") {
      vector<Token> sliced = vector<Token>(cmd.begin() + 1, cmd.end());
      int value = execute_int_expression(sliced);

      cout << value << endl;
    } else if (c.type == "vec") {
      Token variable = cmd.at(1);
      vector<Token> sliced = vector<Token>(cmd.begin() + 2, cmd.end());
      vector<int> values = execute_vector_expression(sliced);

      vector_memo[variable.value] = values;
    } else if (c.type == "print_vec") {
      vector<Token> sliced = vector<Token>(cmd.begin() + 1, cmd.end());
      vector<int> values = execute_vector_expression(sliced);

      cout << "[ ";
      rep(i, values.size()) {
        cout << values.at(i) << " ";
      }
      cout << "]" << endl;
    }
  }

  /*
    rep(i, N) {
      auto cmd = commands.at(i);
      cout << "[" << endl
           << "  ";
      for (auto t : cmd) {
        cout << "{";
        cout << " type: " << t.type << ",";
        cout << " value: " << t.value << " ";
        cout << "}, ";
      }
      cout << endl
           << "]," << endl;
    }
    */

  return 0;
}
