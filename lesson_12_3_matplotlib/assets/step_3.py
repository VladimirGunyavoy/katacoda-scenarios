import matplotlib.pyplot as plt
import numpy as np

year_2021 = np.array([49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62])

plt.plot(year_2021)
plt.title('Прирост клиентов за 2021 год')

# ваш код
...



plt.savefig('my_plot.jpg')