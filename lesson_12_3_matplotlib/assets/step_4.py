import matplotlib.pyplot as plt
import numpy as np

year_2021 = np.array([49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62])

months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

plt.title('Прирост клиентов за 2021 год')
plt.plot(year_2021)

plt.xlabel('месяц')
plt.ylabel('число клиентов в месяц')

# ваш код
...