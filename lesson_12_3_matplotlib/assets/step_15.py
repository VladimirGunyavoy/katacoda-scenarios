import numpy as np
import matplotlib.pyplot as plt

data = {2021: np.array([49, 56, 53, 36, 65, 59, 52, 45, 59, 41, 55, 62]),
        2022: np.array([40, 28, 29, 30, 58, 67, 38, 33, 23, 12, 24, -11]),
        2023: np.array([56, 63, 66, 51, 58, 66, 59, 59, 62, 49, 58, 68])}

plt.figure(figsize=(20, 5))

# ваш код
...

for i, year in enumerate(data):
    plt.subplot(1, 3, i + 1)

    year_data = data[year]

    # ваш код
    ...

    plt.plot(year_data)



plt.savefig('subplot.jpg')