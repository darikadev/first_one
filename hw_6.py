#Задание 1
# a=int(input("Выберите номер месяца:"))
# def season(a):
#     if a== 12 or a==1 or a ==2:
#         print('Зима')
#     elif a==3 or a==4 or a==5:
#         print('Весна')
#     elif a==6 or a ==7 or a==8:
#         print('Лето')
#     elif a==9 or a==10 or a==11:
#         print("Осень")
#     else: print('Ошибка')
# season(a)


# #Задание 2 
# a = int(input('Введите сумму вклада!'))
# years = int(input('Введите  срок '))
# def bank (a,years):
#     count=0
#     final_number=a
#     while count<years:
#         num=a/100
#         num1=num*10
#         final_number+=num1
#         count+=1
#     print(final_number)


# #Задание 3 
# list1=[9,10,5,7,50]
# list2=[15,23,68,74,54]
# def numbers(list1,list2):
#     summ = sum (list1)+sum (list2)
#     final_number=summ/10
#     print(final_number)
# numbers(list1,list2)


#Задание 4 
# def nule(number):

#   for i in range (number):
#      print(f'{i+1}:0')
# number=int(input("Введите число"))
# nule(number)


#Задание 5


# def numbers(list5):
#    i = 0
#    while i < len(list5):
#        if 'A' in list5[i] or 'a' in list5[i] or'I' in list5[i] or'i' in list5[i]:
#             list5.remove(list5[i])
#        else:
#             i+=1


# list5=['Darika','Music','Iphone','Karry','Tom']
# numbers(list5)
# print(list5)


#ДОП ЗАДАНИЕ 2
# def num (n):
#     n=n[::-1]
#     print(n)
# n=input('Введите число')
# num(n)

    
# ДОП ЗАДАНИЕ 3
# def chat(a) :
#     if '?' in a :
#         print('Конечно')
#     elif 'ВОТ ТАК !'in a :
#         print('Успокойся')
#     elif a == "" :
#         print('Как классно когда ты молчишь.Продолжай в том же духе')
#     else:
#         print('ну и что')



# a=input('Напишите что-нибудь')
# chat(a)







