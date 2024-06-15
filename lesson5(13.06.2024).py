immutable_var = tuple([1, 1.5, True, 'Python'])  #Кортеж
print(immutable_var)
print(immutable_var * 2) #Умножение
print(immutable_var + (5, 0, 7))  #Конкатенация
immutable_var_2 = ([11, 12, 15], 1, 2, 3)
print(immutable_var_2) #Список внутри кортежа
immutable_var_2[0][1] = 255 #Обращение к списку и к элементу списка с заменой
print(immutable_var_2)  #Кортеж относится к неизменяемым типам данных, но мы можем обращаться к отедльным элементам. Кортежи поддердивают конкатецию и умножение, есть возможность создать список внутри кортежа

mutable_list = [1, 1.5, True, 'Python']  #Список
mutable_list[0] = 2  #Обращение к элементам списка по инжексу и замена
mutable_list[1] = 2.5
mutable_list[2] = False
mutable_list[3] = 'Java'
print(mutable_list)