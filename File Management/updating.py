# With this mothod, you can change your file contents with starting index from file.seek(..) whatever you give:
# with open("new_file.txt", "r+", encoding="utf-8") as file:
#     file.seek(13)
#     file.write("HEYYY! ")

# Updating at end of the page.
with open("new_file.txt", "a", encoding="utf-8") as file:
    file.write("\nThis is the additionally text!")

# Updating at the beginning of the page
with open("new_file.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "This is the beginning test!\n" + content
    file.seek(0)
    file.write(content)

# Updating file from the middle of the page
with open("new_file.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    lines.insert(1, "This will be my middle text!\n")
    file.seek(0)
    # for line in lines:    # we can use this method, or use writelines()
    #     file.write(line)
    file.writelines(lines)

with open("new_file.txt", "r", encoding="utf-8") as file:
    print(file.read())
