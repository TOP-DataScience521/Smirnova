from datetime import datetime


name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")

current_year = datetime.now().year
# УДАЛИТЬ: избыточная операция
print()

age = int(current_year) - int(birth_year)

print(surname, name + ',', age)


# Введите ваше имя: Елена
# Введите фамилию: Смирнова
# Введите год рождения: 1978
# 
# Смирнова Елена, 47


# ИТОГ: 1/2


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/

