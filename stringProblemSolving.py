# a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# print(a.replace(".", ""))
# print(a.split("."))
# print(sorted(a))
# print(a.count("O"))
#
# z = "F.R.I.E.N.D.S"
# print(z.strip(".,"))

str = input("please enter a string")
print(str[::-1])

print(str.isdigit())
print(str.istitle())

reverse = str[::-1]
if reverse == str:
    print("palindrome")


