# Задача 1
# age = int(input("Введите свой возраст."))
# if (age < 18):
#     print("Вы являетесь несовершеннолeтним!")
# elif age <= 18 :
#     print ("Вы являетесь совершеннолетним!")
# elif age >= 65 :
#      print("Вы являетесь пожилым")
# elif age <=18_65:
#      print("Вы являетесь совершеннолетним!")
#  # Задача 2
# number1= int(input("Введите  первое число"))
# number2= int(input("Введите второе число"))
# number3= int(input("Введите третое число"))
# if number1>number1 and number2:
#     print(number1)
# elif number3>number2 and number1>number2:
#     print(number2)
# elif number1>number3 and number2>number3:
#     print(number3)
# Задача 3
# hw_list = ['Osh','Bishkek','Chicago','London','toyota','Lexus','KIA','Selena','Justin','Kylie','Jackson','Mitsubishi','Weekend','Honda','BMW','Adele']
# print (hw_list[2:7])
#Задача 4   
# list = ['Darika','Erlan','Aisha','Dias','Toyota','Lexus','BMW','Honda','Chevrolete','Lada']
# print(list)
# list.pop(2)
# print(list)
# list.pop(8)
# print(list)
# list.append("Lemon")
# list.append("Banana")
# list.append("Orange")
# list.append("Tomato")
# list.append("Strawberry")
# print(list)
#Задача 5
# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(numbers)
# numbers.pop(2)
# print(numbers)
# numbers.remove(16)
# print(numbers)
# numbers.insert(0,5)
# print(numbers)
# numbers.insert(1,9)
# print(numbers)
#задача 6 и 7 и 8
# numbers_list = [2,3,1,52,56,8,3,58,0,98,75,3,45,2,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,3,6,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,0,654,235,65,23,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,132,321,452,3,]
# numbers_list.sort()
# print(numbers_list)
# numbers_list.reverse()
# print(numbers_list)
# numberslist = [2,3,1,52,56,8,3,58,0,98,75,3,45,2,44,2,1,4,5,6,8,909,4,24,653,12,43,2,5,3,6,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,0,654,235,65,23,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,132,321,452,3,]
# print(numberslist)
# print(numberslist.count(2))
# print(numberslist.count(5))
# print(numberslist.count(3))
# Задание 9
# import statistics
import statistics


list =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
average=statistics.mean(list)
print("list:", average)
#Дополнительные задания
# numbers = [1,2,3,4,5,6,7,8,9,10,]
# min_digit=min(list(numbers))
# print (min_digit)
# numbers = [1,2,3,4,5,6,7,8,9,10,]
# max_digit=max(list(numbers))
# print(max_digit)

#Задача 4
# print(sum(numbers))
# print(numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]+numbers[5]+numbers[6]+numbers[7]+numbers[8]+numbers[9])



#Задача 5
# music = ['Believer','Thunder','Chandelier','Monster','Love','Fade','King','Dimonds','Slow down','Dance Monkey']
# #          0            1           2           3       4       5      6    7           8           9
# music[4], music[8] = music[8], music[4]
# print(music)



#Задача 6
# numbers= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
