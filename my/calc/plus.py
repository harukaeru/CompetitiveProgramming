import re

tokenizers = [
    ['number', r'\d+'],
    ['space ', r' +'],
    ['plus', r'\+'],
    ['minus', r'-'],
    ['multiply', r'\*'],
    ['divide', r'\\'],
]

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'<{self.name}: {self.value}>'

def tokenize(s, pos, tokens=[]):
    if pos == len(s):
        return tokens

    next_string = s[pos:]
    for token_name, token_regex in tokenizers:
        matched = re.match(token_regex, next_string)
        if not matched:
            continue
        start, end = matched.span()
        new_token = Token(token_name, next_string[start:end])
        tokens.append(new_token)
        pos += end
        return tokenize(s, pos, tokens)
    raise SyntaxError(f'{pos}: {s[pos:]}')

s = input()

print(tokenize(s, 0))

def parse_expression(tokens):
    expression = {
        'nodes': [],
        'calc': None
    }

    for token in tokens:
        if token.name == 'number':
            expression.nodes.append(token)

class Syntaxer:
    def __init__(self, token, parent):
        self.token = token
        self.parent = parent

def analyze_syntax(tokens):
    for token in tokens:
        syntaxer = Syntaxer(token, parent)
        syntaxer.

