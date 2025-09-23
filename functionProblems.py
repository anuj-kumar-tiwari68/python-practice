# write a function to find maximum of three numbers
# def maximum_num(val1,val2,val3):
#     if val1 > val2 and val1 > val3:
#         return val1
#     elif val2 > val1 and val2 > val3:
#         return val2
#     else:
#         return val3
# print(maximum_num(1,22,3))
# write a function to create and print a list where the values are squares of numbers between 1 and 30
#
# def l():
#     list = []
#     for i in range(1,31):
#         list.append(i*i)
#     return list
# print(l())


# write a function that takes a number as a perimeter and check if the number is prime or not
# def prime(num):
#     if num == 1:
#         print("not prime")
#     if num == 2:
#         print("prime")
#     if num > 2:
#         for i in range(2,num):
#             if num % i == 0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#
# prime(37)


# write a function to sum all the numbers in a list
# def add(num):
#     total = 0
#     for i in num:
#         total += i
#     return total
# print(add([12,12,33,4,55,66]))

# solution 2 using recursion
# def add(num):
#     if len(num) == 1:
#         return num[0]
#     else:
#         return num[0] + add(num[1:])
# print(add([12,12,33,4,55,66]))


# write a python program to solve a fibonacci sequence using recursion

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))