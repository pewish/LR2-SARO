import numpy as np
from scipy.optimize import linprog

# Коэффициенты целевой функции
c = np.array([-5, -4])

# Коэффициенты левых частей ограничений
A = np.array([
    [-1, 1],
    [1, -2],
    [2, 1]
])

# Правые части ограничений
b = np.array([1, 1, 22])

# Знаки ограничений (≤ заменяется на = и добавляется -1 для минимизации)
signs = ['>=', '>=', '>=']

# Решение двойственной задачи
dual_solution = linprog(c, A_ub=-A, b_ub=-b, method='highs')

# Оптимальное решение двойственной задачи
optimal_dual = dual_solution.x

# Значение целевой функции двойственной задачи
optimal_dual_value = -dual_solution.fun

# Вывод результатов
print("Оптимальное решение двойственной задачи:")
print("y1 =", optimal_dual[0])
print("y2 =", optimal_dual[1])
print("y3 =", optimal_dual[2])
print("Значение целевой функции двойственной задачи:", optimal_dual_value)
