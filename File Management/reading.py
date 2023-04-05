file = open("new_file.txt", "r", encoding="utf-8")

# we can take the contents with a for loop
for i in file:
    print(i)

# we can use read function as well
# Here, we should re-open file because at the above, the cursor read the all line and put itself to the end of the file. So, we should go beginning of the file.
file = open("new_file.txt", "r", encoding="utf-8")
content = file.read()
# content = file.read(5) reads 5 characters.
print(content)

# using readline()
file = open("new_file.txt", "r", encoding="utf-8")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline())

# using readlines()
file = open("new_file.txt", "r", encoding="utf-8")
myList = file.readlines()
for line in myList:
    print(line)

file.close()
