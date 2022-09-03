#!/usr/bin/env python3
import sys
import os
import random

##############################################################################

# config
IN_TXT_START = 5
IN_TXT_END = 60
EXECUTION_COMMAND = './to_test.py'

input_template = '''
{L} {R}
'''

def create_context():
    ctx = dict()
    ctx['L'] = random.randint(1, 2019)
    ctx['R'] = random.randint(ctx['L'] + 1, 4040)
    return ctx

##############################################################################

def generate_test():
    for i in range(IN_TXT_START, IN_TXT_END + 1):
        ctx = create_context()
        input_string = input_template.format(**ctx).strip() + '\n'

        in_file = f'in_{i}.txt'
        out_file = f'out_{i}.txt'
        print('.', end='', flush=True)
        with open(in_file, 'w') as f:
            f.write(input_string)
        os.system(f'cat {in_file} | {EXECUTION_COMMAND} > {out_file}')
    print()

# usage:
# $ python3 random_test.py

generate_test()
