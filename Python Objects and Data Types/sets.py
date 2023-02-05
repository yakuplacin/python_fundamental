fruits = {"orange", "apple", "banana"}
#This is a SET, different than dictionary. AND YOU CANNOT ADD THE VALUE THAT IS ALREADY EXIST
# you cannot achive with fruits[0]  XXXXX

for x in fruits:
    print(x)

fruits.add("Kiwi")
fruits.update(["mango", "grape"])
print(fruits)

#if you try to add the value that already exists, it will be not counted Becuase it is a SET!!!!!!!
#FOR EXAMPLE:

fruits.add("orange") ##it will change nothing! it will not add I mean

fruits.remove("mango")
fruits.discard("apple")
fruits.pop()  ##as it is a set, it deletes randomly not the last elemen like the array!!
print(fruits)

myList = [1,2,3,4,5,1,2,3,4,5]
print(myList)
myList2 = set(myList)  #it will take number distinct
print(myList2)

