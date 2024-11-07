import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

# Чтобы заменить значение NaN, нужно использовать команду fillna, заполняющую
# все пропуски.

df.fillna(0, inplace=True)

print(df)


# можно их удалить значение NaN. Удалится вся строка

# df.dropna(inplace=True)
# print(df)


# ----------------------------------------------------------------
''''
Как удалить строку с определенным индексом (или номером ) в DF ?

У DataFrame есть метод drop, которому нужно передать список индексов, например,
df.drop([0]) удалит первую строку (если у вас RangeIndex)
'''''




# среднюю продолжительность жизни животных в зависимости от того, чем они питаются.
# Для создания группы мы используем переменную group, для подсчёта среднего значения — mean:

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

# сохранить изменения в таблицах (удаление и добавление столбцов, строк и т.д.),
# необходимо использовать функцию to_csv, а в круглых скобках указать место сохранения:

df.to_csv('output.csv', index=False)
