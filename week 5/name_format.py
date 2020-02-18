fullname = list(input(). split ())

last_name = fullname[-1]
first_name = list(fullname[0])[0]
if len(fullname) < 3:
    print(last_name, end=',')
    print('',first_name,end='.\n')
else:
    middle_name = list(fullname[1])[0]
    print(last_name, end=',')
    print('',first_name,end='.')
    print(middle_name,end='.\n')