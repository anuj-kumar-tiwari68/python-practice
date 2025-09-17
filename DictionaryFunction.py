# Student = {"name":"John", "class":"6th","roll":23}
#get => gives the particular key's value
# x = Student.get("name")
# print(x)

#item => keys values in tuple forms
# a = Student.items()
# print(a)

#keys
# b = Student.keys()
# print(b)
# #values
# c = Student.values()
# print(c)
#
# #copy
# d = Student.copy()
# print(d)

# ++++++++++++++++++++++++++ part 2 +++++++++++++++++++++++++++
Student = {"name":"John", "class":"6th","roll":23}
#setdefault
x = Student.setdefault("roll",24)
print(x)

#update
#pop
#popitem
#clear