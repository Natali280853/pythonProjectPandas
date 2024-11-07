import pandas as pd


data = { 'Name': ['Alice', 'Bob', 'Roma', 'Anna'], 'Age': [23, 45, 17, 24], 'City': ['New York', 'LA', 'Chicago', 'Moscow'] }

df = pd.DataFrame(data)
print(df)
print()

# ------------------------------------------
# удалить строку
df = df.drop(1)
print(df)



print(f"df.index {df.index}")

# df.index = ['a', 'b', 'c', 'd']
df.index = ['a', 'b', 'c']
print(f"df.index {df.index}")
print(df)

df_reset = df.reset_index(drop=True)
print(df_reset)

# НЕ РАБОТАЕТ
df.rename(columns = {'Age' : 'Vozrast'})
print(df)

#  РАБОТАЕТ !!!!
df.columns = [it.replace('Age', 'Vozrast') for it in df.columns]
print(df)


df.to_csv('output.csv', index=False)






# ---------------------------------------------------------------------------

# Что касается метода isin, то это та же операция, что и оператор in в Python,
# применимый для итерируемых объектов. Т.е. он проверяет присутствует ли
# в DataFrame или Series тот или иной элемент. Из примера, может нагляднее будет
# такой код

# df[df['A'].isin([1,3])]

# Т.е. тут применяется фильтр к столбцу A, проще говоря, верни мне строки,
# где в A есть значения 1 или 3.