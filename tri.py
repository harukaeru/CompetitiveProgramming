STEP_COUNT = 12
MAX_WIDTH = 36
for step_index in range(STEP_COUNT):
    symbol_width = MAX_WIDTH - step_index * (MAX_WIDTH // STEP_COUNT)
    space = ' ' * ((MAX_WIDTH - symbol_width) // 4)
    symbol = '@*' * (symbol_width // 2) + '@' * (symbol_width % 2)
    rendered = space + symbol
    print(rendered)
