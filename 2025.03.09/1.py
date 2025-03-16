name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")

from datetime import datetime
current_year = datetime.now().year
print()

age = int(current_year) - int(birth_year)

print(surname, name + ',', age)


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.09
 # 13:43:56 > python 1.py
# Введите ваше имя: Елена
# Введите фамилию: Смирнова
# Введите год рождения: 1978

# Смирнова Елена, 47
