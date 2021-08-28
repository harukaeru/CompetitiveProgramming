import sys

for i, line in enumerate(sys.stdin):
    case_idx = i + 1
    num = line.replace('\n', '')
    if num == '0':
        exit()
    print(f"Case {case_idx}: {num}")

