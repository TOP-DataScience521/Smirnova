num1 = int(input('число: '))

# УДАЛИТЬ: избыточная переменная
num2 = 1

# УДАЛИТЬ: избыточные операции
res1 = f'{num1 + num2}'
res2 = f'{num1 - num2}'

# ИСПРАВИТЬ: вывод не соответствует требуемому формату
print('Следующее за числом', num1, 'число: ', res1, '\nДля числа', num1, 'предыдущее число: ', res2)
# КОММЕНТАРИЙ: в случае, если вы будете генерировать строку не для чтения человеком, а для другой функции/класса/программы — неверный формат может стоить вам неработающего приложения


# число: 65
# Следующее за числом 65 число:  66
# Для числа 65 предыдущее число:  64


# ИТОГ: 1/2

