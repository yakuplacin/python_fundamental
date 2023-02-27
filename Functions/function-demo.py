# def writeWord(count, word):
#     for i in range(count):
#         print(word)
# we also use this
#     print(word * count) # it is so basic!!!!!
       

# writeWord(4, "Gözde")

# result = []

# def switchList(*params):
#     for item in params:
#         result.append(item)
# or create a list = [], and return this is also possible

# switchList(1, 234, "Yakup", 23, 4, "asd", "Gözde", 32,
#            345, 43, 32, 34, 6, 42, 34, 2123, 44, 576,)
# print(result)

# primary = []

# def findPrimary(nm1, nm2):
#     for i in range(nm1, nm2):
#         isPrim = True  ##don't need this
#         if i > 1:
#             for x in range(2, i):
#                 if i % x == 0:
#                     isPrim = False ##dont need this line
#                     break
#####         (primary.append(i), print("Hit ", end="-")) if isPrim else print("Miss ", end="-")  
#              else:  #we may also use this else that belongs to the for loop!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                  primary.append(i)         

# findPrimary(2, 11)
# print("\n{}".format(primary))

# def intDivider(num):
#     list = []
#     for item in range(1,num):
#         if num % item == 0:
#             list.append(item)
#     return list
# myList = intDivider(20)
# print(myList)