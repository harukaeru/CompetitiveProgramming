func_wrapper_line = '@profile\ndef main():\n'
lines = list(open('main.py').readlines())

insert_pos = 0
if lines[0].startswith('#!'):
    insert_pos = 1

generated_lines = []
for i, line in enumerate(lines):
    if i == insert_pos:
        generated_lines.append(func_wrapper_line)

    if i < insert_pos:
        generated_lines.append(line)
    if i >= insert_pos:
        if line.startswith('def'):
            generated_lines.append('  @profile\n' + '  ' + line)
        else:
            generated_lines.append('  ' + line)

generated_codes = ''.join(generated_lines)
print(generated_codes)
gen = compile(generated_codes, 'kerorin.py', 'exec')
data = {}
exec(gen, data)
# print(data['main'])
with open('kerorin.py', 'w') as f:
  f.write(generated_codes)

main_func = data['main']
print('---------- Result -----------')
main_func()
print('----------  END  ------------')
