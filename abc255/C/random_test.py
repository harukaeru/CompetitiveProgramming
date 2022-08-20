#!/usr/bin/env python3
import sys
import os
import random

# config
IN_START = 5
IN_END = 60
EXECUTION_COMMAND = './to_test.py'

##############################################################################

input_template = '''
{X} {A} {D} {N}
'''

def create_context():
    ctx = dict()
    ctx['X'] = random.randint(-10 ** 3, 10 ** 3)
    ctx['A'] = random.randint(-10 ** 3, 10 ** 3)
    ctx['D'] = random.randint(-10 ** 3, 10 ** 3)
    ctx['N'] = random.randint(-10 ** 3, 10 ** 3)
    return ctx

##############################################################################

def generate_test():
    for i in range(IN_START, IN_END + 1):
        ctx = create_context()
        input_string = input_template.format(**ctx).strip()
        print(f'Generating in_{i}.txt & out_{i}.txt ...')
        with open(f'in_{i}.txt', 'w') as f:
            f.write(input_string)
        os.system(f'cat in_{i}.txt | {EXECUTION_COMMAND} > out_{i}.txt')

# usage:
# $ python3 random_test.py test

generate_test()
if len(sys.argv) > 1:
    os.system('atcoder-tools test')
