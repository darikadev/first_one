# users = ("Nurbolot","Darika", "Anton")
# print(type(users))
# users_list= list(users)
# print(type(users_list)) 
# users_list.append("Geeks")
# users_list.remove("Anton")
# print(users_list)
# users_list=tuple(users_list)
# print(users_list)
# users_list[1]

# student={'name': "Beksultan", "age":'20', "from": 'kyrgyzstan'}
# dop_info = {'hobby': "Singing"}
# print(student)
# print(f"Имя:{student['name']}")
# print(f"Возраст;{student['age']}")
# print(f"Место рождения:{student['from']}")

# print(student)
# student['job'] = "Developer"
# print(student)
# student['name'] = "Darika"
# del student['from']
# print(student)
# student.update(dop_info)
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# student.pop("name")
# print(student)
   

# Множества = set,frozenset
#создается с помощью фигурных скобок
# Не имеет структуры и определенного порядка
# Не  можем использовать индексы и срезы
#Не имеет дубликатов
# set - Изменяемый 
#frozenset - неизменяемый
# users={"Nurbolot","Beksultan","Beksultan" ,"Geeks", "Geeks","Darika"}
# print(users)
# users.add("Lira")
# print(users)
# # print(users[1]) не работает
users = frozenset(["Nurbolot","Vlad","Georgiy","Ilya"])
print(type(users))
users_set =(set(users))
users_set.remove("Vlad")
print(users_set)
users_set =(frozenset(users))
print(users_set)