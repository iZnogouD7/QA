# abclist=["samir","samir","roshan","bijaya","bibhu"]
# print(abclist)
# print(len(abclist))
#
# mixed_list=[1,2,"samir","bijaya",2055,True,"bibhu"]
# print(mixed_list)
# print(len(mixed_list))
# print(mixed_list[0])#start index from 0
# print(mixed_list[3])
# print(mixed_list[-1])#last index starts from -1
# print(mixed_list[-3])
# #print(mixed_list[-9])#list index out of range
# print(mixed_list[2:5])# slicing, first is inclusive last is exclusive
#
# if ("bibhu" in mixed_list):
#     print("Yes bibhu is Here")
# print("Absent")
# if ("bibhu" in mixed_list):
#     print("Yes bibhu is Here")
#     if "samir" in mixed_list:
#         print("Yes samir is Here")# yo loop bhitra janaw first if condition must satisfy
# elif ("bijaya" in mixed_list):
#     print("Yes bijaya is Here")
# else:
#     print("Not present")

a=2000
b=12000
#short hand if condition for if else
print("A is greater than B") if a>b else print("b is greater than a")
# for if else
print("A is greater than B") if a>b else print("b is greater than a") if a<b else print("They are Equal")
