# for item in range(50,100,10):
#     print(item)

# print(list(range(5,100,10)))

#
# enumerate
#

# greeting = "Hello!"

# for index, item in enumerate(greeting):
#     # print(item[1])
#     print (f"index: {index} letter: {item}")

# index = 0
# greeting = "Hello!"

# for letter in greeting:
#     print(f"index : {index} letter: {greeting[index]}")
#     index += 1

#
# zip
#
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300, 400, 500]
print(list(zip(list1, list2, list3)))  # tuple

for item in zip(list1, list2, list3):
    # print(item)
    print(f"list1: {item[0]} list2: {item[1]} list3: {item[2]}")

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)