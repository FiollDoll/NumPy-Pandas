import numpy as np
"""
numbers = [1, 2, 3, 4]

array = np.array(numbers) #Получение списка
print(array)
"""

"""
zero = np.zeros(3) #создание 3 нуля
print(zero)
"""

"""
one = np.ones(3) #создание 3 единиц
print(one)
"""

"""
#Прибавление
data = np.array([1,2])
ones = np.ones(2) #1 1
data = data + ones # 2. 3
print(data)
"""

"""
data = np.array([1.9, 2.3])
ones = np.ones(2)
data = data - ones
print(data)
"""

"""
data = np.array([1, 2, 3, 4])

print(data.max()) #Выводит большее
print(data.min()) #Выводит меньшее
print(data.sum()) #Прибавляет
"""

"""
data = np.array([1, 2, 3, 4])
random = np.random.random(4) #Выдаёт рандомные числа на сумму 4
data = data + random
print(data.max()) #Выводит большее
"""
#https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
#https://python-scripts.com/numpy
"""
#Создание матрицы
array = np.array([[1,2],[3, 4]])
print(array)
"""

"""
#Создание матрицы из однёрок
one = np.ones((2,3)) #2 - высота, 3 - ширина
print(one)
"""

"""
#Пример
one = np.ones((2,2)
data = np.array([[2,4], [5, 6]])
data = data - one
print(data)
#[[1. 3.]
 [4. 5.]]
#Но можно так:
#p.s NumPy переменную one(столбец) применяет на все
one = np.ones(2)
data = np.array([[2,4], [5, 6]])
data = data + one
print(data)
"""