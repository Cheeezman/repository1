
import numpy as np
from scipy.interpolate import splrep

# Задаем точки
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 1, 3, 2, 4])

# Находим коэффициенты сплайна
tck = splrep(x, y)

# Распаковываем коэффициенты сплайна
c, b, a = tck[0], tck[1], tck[2]

# Выводим найденные коэффициенты сплайна
print('Коэффициенты a:', a)
print('Коэффициенты b:', b)
print('Коэффициенты c:', c)
