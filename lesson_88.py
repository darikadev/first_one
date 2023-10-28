# file_write = open ('Geeks.txt','w')
# file_write.write("Всем привет меня зовут Дарика")
# file_write.close()


# test=open("user.txt",'w')
# test.write("This is test work!!!")
# test.close()


# while True:
#     for i in range(1,25):
#      hacking=open(f"haha{i}.txt","w")
#      hacking.write("Вас взломали")


name=input("Введите имя")
age=int(input("Введите возраст"))
phone=int(input("Введите телефонный номер"))
users=open("users.txt",'w')
users.write(f"Имя:{name}, Возраст {age}, Номер:{phone}")
users.close()