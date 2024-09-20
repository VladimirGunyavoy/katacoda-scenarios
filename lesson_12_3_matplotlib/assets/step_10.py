import matplotlib.pyplot as plt
import numpy as np

months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

year_2021 = np.array([49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62])

mean = year_2021.mean()

plt.title('Прирост клиентов за 2021 год')

plt.plot(year_2021, label='прирост клиентов')

# ваш код
plt.plot(...)

plt.xlabel('месяц')
plt.ylabel('число клиентов в месяц')
plt.xticks(ticks=range(len(months)), labels=months)
plt.grid()
plt.legend()