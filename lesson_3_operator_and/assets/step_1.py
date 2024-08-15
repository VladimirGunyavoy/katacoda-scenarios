# темная магия для получения броска монетки
# и вывода значения
# ничего не меняйте
import numpy as np
coin1 = bool(np.random.randint(0, 2))
coin2 = bool(np.random.randint(0, 2))
print('coin 1:', coin1)
print('coin 2:', coin2)
print()

# ваш код
if coin1 and coin2:
    print('True')
else:
    print('False')