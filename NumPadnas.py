import pandas as pd
import numpy as np

"""
name = input("Ваше имя: ")
answer = input("4 + 4 = ")
df = pd.DataFrame({
    "Name": [name],
    "otvet": [answer]
})

#Сохранение в Блокнот
df.to_csv("man.csv") #Криво сохраняется
print(df)
#Сохранение в Ексель
writer = pd.ExcelWriter("man.xlsx") #Нормально сохраняется
df.to_excel(writer)
writer.save()
"""

pet = ["Кот", "Собака", "Питон", "Попугай"]
array = np.array([[1,4], [3, 5]])
df = pd.DataFrame({
    "Pet": pet,
    "count": array.ravel() # "вытягиваем" матрицу в одномерный вектор
})