
with open('abs_func.py')as f:
    lines = f.read()

code_obj = compile(lines, 'abs_func.py','exec')
exec(code_obj)
