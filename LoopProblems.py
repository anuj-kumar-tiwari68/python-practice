# program to find sum of all even numbers upto 50
# sum = 0
# for i in range(0,51):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# program to write first 20 numbers and their squares

# for i in range(1,21):
#     print(i," ",i**2)


# program to find sum of first 10 odd numbers using while loop
# num = 1
# s = 0
# while num < 21:
#     if num % 2 == 1:
#         s += num
#     num += 1
# print(s)

# for i in range(1,101):
#     if i % 8 ==0 and i % 12 == 0:
#         print(i)

# billing system at supermarket

# while True:
#     name = input("Enter your name: ")
#     total = 0
#     while True:
#         quantity = int(input("Enter your quantity: "))
#         amount = float(input("Enter your amount: "))
#         total += quantity * amount
#         repeat = input("Do you want to repeat? (Y/N): ")
#         if repeat == "no" or repeat == "No":
#             break
#     print("-"*40)
#     print("Name:", name)
#     print("Total amount to be paid:", total)
#     print("-"*40)
#     print("*******HAPPY SHOPPING********")
#     repeat1 = input("Do you want to go to next customer? (Y/N): ")
#     if repeat1 == "no" or repeat1 == "No":
#         break

for i in range(1,11):
    for j in range(1,i+1):
        print(i,end = " ")
    print()