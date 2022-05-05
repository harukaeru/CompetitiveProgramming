echo_lines = open('all_f_options.txt.echo').readlines()
time_lines = open('all_f_options.txt.time').readlines()

for i, echo_line in enumerate(echo_lines):
    time_line = time_lines[i]
    echo_line = echo_line.replace('\n', '')
    time_line = time_line.replace('\n', '')

    print(echo_line + " && " + time_line)
