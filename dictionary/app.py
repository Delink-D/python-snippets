def print_ninjas(dic):
    for key, value in dic.items():
        print(key + ' is a ' + value + ' developer')

ninjas = {}

while True:
    ninja_name = input('Provide the ninja name ')
    ninja_language = input('Which language? ')

    ninjas[ninja_name] = ninja_language

    add_another = input('Do you wish to add another Ninja? (y/n) ')

    if add_another == 'y':
        continue
    else:
        break

print_ninjas(ninjas)
