try:
    num = int(input('число: '))
except ValueError:
    print('не является чиcлом')
    exit()
if num < 0 or num > 10:
    print('нет')
    exit()

if num > 0 and (num & (num - 1))== 0:
    
# res = num ** 0.5
# if (res == int(res)) and (int(res) == num // 2):
    
    print('да')
else:
    print('нет')
    
    
    # C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 19:29:44 > python 4.py
# число: 4
# да


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 19:30:02 > python 4.py
# число: 1
# да


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 19:30:28 > python 4.py
# число: -8
# нет


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 19:30:32 > python 4.py
# число: abc
# не является чиcлом