# c
# result =list(map(lambda  num:lambda a:a*2, numbers))
# print(result)

# # numbers = [1,2,3,4,5]

# # def result (numbers):
# #     result_numbers=[]
    
# #     for num in numbers:
# #        result_numbers.append(num*2)
# #        return(result_numbers)
    

# # print(result(numbers))

# # numbers = lambda a,b : a-b
# # print(numbers(10,5))


# def numbers(a,b):
#  print(a-b)
# a=10
# b=5
# numbers(a,b)

# def numbers(a,b,):
#     print(a-b)
#     a=5
#     b=6
   
# numbers(10,50)


# def reverse(numbers):
#     print(numbers[::-1])

# numbers=[1,2,3,4,5,6,7,8,9,10]
# reverse(numbers)

# reversed = list(map(lambda x:x[::-1],[[1,2,3,4,5,6,7,8,9,10]]))
# print(reversed)
 

# summ = lambda num1,num2:num1*num2
# print(summ(2,4))

# # def summ (num1,num2):
# #     print(num1+num2)


names=['Meergul','Beksultan','Islam','Vlad']
result=list(map(lambda num:f'{num}- {len(num)}букв',names))
print(result)


# def result(names):
#     result_names=[]
#     for num in names:
#        result_names.append (f"{num}" - {len(num)} букв")
#                             print(result(names))

# names=['Meergul','Beksultan','Islam','Vlad']
# result=list(map(lambda num: num.upper(), names))
# print(result)


#try except
# try:
# n =0
# n2 =2 
# print(n2/n)
while True:

    try:
        num1=int(input("Введите число:"))
        num2=int(input("Введите второе число:"))
        print(num1/num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя, иди учи математику ")
    except ValueError:
       print("Не пиши буквы")



