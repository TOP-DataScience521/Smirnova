a = int(input('введите число 1: '))
b = int(input('введите число 2: '))

# ИСПРАВИТЬ: одинаковые операции в большинстве случаев имеет смысл выполнить заранее
print(f'\n{a} делится на {b} нацело\nчастное: {a // b}' if not a % b else f'\n{a} не делится на {b} нацело\nнеполное частное: {a // b}\nостаток: {a % b}')


# введите число 1: 10
# введите число 2: 2
# 
# 10 делится на 2 нацело
# частное: 5


# введите число 1: 12
# введите число 2: 5
# 
# 12 не делится на 5 нацело
# неполное частное: 2
# остаток: 2


# ИТОГ: 3/4

