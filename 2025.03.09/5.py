num1 = (input('Введите целое число 1: '))
num2 = (input('Введите целое число 2: '))
km = 1.61
ml = float(str(num1) + "." + str(num2))
km_all = km * ml
print(f'{ml:.2f} миль =', f'{km_all:.1f} км')




# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.09
 # 18:22:41 > python 5.py
# Введите целое число 1: 85
# Введите целое число 2: 65
# 85.65 миль = 137.9 км
