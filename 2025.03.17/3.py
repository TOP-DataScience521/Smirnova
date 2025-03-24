year = int(input('введите год: '))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0): 
    print('да') 
else: 
    print('нет')
    
# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 14:57:08 > python 3.py
# введите год: 2020
# да


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 14:57:24 > python 3.py
# введите год: 2000
# да


# C:\Users\DmMSTR\Documents\DataScience521\Smirnova\2025.03.17
 # 14:57:31 > python 3.py
# введите год: 1978
# нет