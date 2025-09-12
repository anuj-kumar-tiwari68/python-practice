# write a program to check if a number is positive or not


num = int(input("enter a number"))
if num >0:
    print("number is positive")

# program to check weather a number is odd or even
num1 = int(input("enter a number"))
if num1 % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# program to create area of circle

num2 = int(input("enter a number"))
area = 3.14 * num2 * num2
print("area of circle is : ",area)

# program check weather the passed letter is a vowel or not

vowels = "aeiouAEIOU"
char = input("enter a character")
print("character entered is vowel") if char in vowels else print("character entered is not vowel")

# program to check weather a number is single digit, two digit .... upto 5 digit number

num3 = int(input("enter a number upto 5-digit"))
if (0<= num3 <= 9) or (-1 >= num3 >= -9):
    print("number is single digit number")
elif (num3 >=10 and num3 <= 99) or (num3 <= -10 and num3 >= -99):
    print("number is double digit number")
elif (num3 >=100 and num3 <= 999) or (num3 <= -100 and num3 >= -999):
    print("number is 3-digit number")
elif (num3 >=1000 and num3 <= 9999) or (num3 <= -1000 and num3 >= -9999):
    print("number is 4-digit number")
elif (num3 >=10000 and num3 <= 99999) or (num3 <= -10000 and num3 >= -99999):
    print("number is 5-digit number")
else:
    print("enter a 5-digit number or less")
