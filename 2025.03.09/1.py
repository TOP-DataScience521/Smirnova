from datetime import datetime


name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")

current_year = datetime.now().year
print()

age = int(current_year) - int(birth_year)

print(surname, name + ',', age)


# Введите ваше имя: Елена
# Введите фамилию: Смирнова
# Введите год рождения: 1978
# 
# Смирнова Елена, 47

