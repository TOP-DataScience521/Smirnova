...
===== 1 =====
name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")
from datetime import datetime
current_year = datetime.now().year
print()
age = int(current_year) - int(birth_year)
print(name, surname, end=', ')
print(age)

...
===== 2 =====
num1 = int(input( ))
num2 = 1
res1 = f'{num1 + num2}'
res2 = f'{num1 - num2}'
print(' Следующее за числом', num1,'число: ', res1,'\n', 'Для числа', num1, 'предыдущее число: ', res2)