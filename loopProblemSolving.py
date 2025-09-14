# fibonacci series
# a = 0
# b = 1
# n = int(input("please enter your number: "))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# number is prime or not
# import math
# count = 0
# n = int(input("please enter a number: "))
# if n < 2:
#     print("not a prime")
# else:
#     isPrime = True
#     for i in range(2,int(math.sqrt(n))+1):
#         if n % i == 0:
#             isPrime = False
#             break
#     if isPrime:
#         print("prime")
#     else:
#         print("not a prime")


# palindrome
num = int(input("please enter a number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if reverse == temp:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

