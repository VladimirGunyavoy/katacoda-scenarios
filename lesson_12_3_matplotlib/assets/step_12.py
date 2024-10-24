import numpy as np
import matplotlib.pyplot as plt

months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

year_2021 = np.array([49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62])

mean = year_2021.mean()

# ваш код
...
...



plt.title('Прирост клиентов за 2021 год')

plt.plot(year_2021, 'o', label='прирост клиентов')
plt.plot(year_2021, linestyle='--')

plt.plot(mean * np.ones(len(year_2021)),
         linestyle='-.',
         label=f'mean: {mean.round(1)}')


# Ваш код
...


# Ваш код
...



plt.xlabel('месяц')
plt.ylabel('число клиентов в месяц')
plt.xticks(ticks=range(len(months)), labels=months)
plt.grid()
plt.legend()

plt.savefig('my_plot.jpg')