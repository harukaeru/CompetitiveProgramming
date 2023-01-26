STEP_COUNT = 50
MAX_WIDTH = 100
for step_index in range(STEP_COUNT):
    symbol_width = MAX_WIDTH - step_index * (MAX_WIDTH // STEP_COUNT)
    space = ' ' * ((MAX_WIDTH - symbol_width) // 2)
    symbol = '*' * symbol_width
    rendered = space + symbol
    print(rendered)
