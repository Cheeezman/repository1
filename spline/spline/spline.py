
import numpy as np
from scipy.interpolate import splrep

# ������ �����
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 1, 3, 2, 4])

# ������� ������������ �������
tck = splrep(x, y)

# ������������� ������������ �������
c, b, a = tck[0], tck[1], tck[2]

# ������� ��������� ������������ �������
print('������������ a:', a)
print('������������ b:', b)
print('������������ c:', c)
