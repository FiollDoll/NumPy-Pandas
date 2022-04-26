import pandas as pd
import numpy as np

df = pd.DataFrame ({ #Содаём таблицу
     "Name": ["Artem", "Anton"], #Значения
     "Balance": ["100", "0"],
     "Age": ["14", "5"]
})

print(df, "\n") #Полностью
print(df[["Name", "Age"]], "\n") #Выбранное
"""
#Способы сохранения информации и сбора

#Сохранение в Ексель
writer = pd.ExcelWriter("name.xlsx")
df.to_excel(writer)
writer.save()

#Чтение csv
data = pd.read_csv("name.csv") #Через файл. Первая строка - значение

print(data)

#Чтение Екселя
data1 = pd.read_excel("info.excel") #Ексель
print(data1)
"""