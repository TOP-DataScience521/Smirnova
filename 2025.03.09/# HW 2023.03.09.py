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
