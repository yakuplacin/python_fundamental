# To open a file, open() function is used.
# usage: open(file_name, file_access_mode)
# file_access_mode is about which purpose we open the file.

# 'w': Write mode. File is created in the current path. It deletes the contents of existing file.
# 'a': Append mode. File is created if it does not exist in the current path.
# 'x': Create mode. If file exists, it gives an error.
# 'r': Read mode. It is default mode. If file does not exist in the current path, it gives an error.

file = open("new_file.txt", "w", encoding='utf-8')
file.write("Hello WORLD!\n")
file.close()  # Close the file after dealing with it.

file = open("new_file.txt", "a", encoding='utf-8')
file.write("This will be the text!")
file.close()

file = open("new_file2.txt", "x", encoding='utf-8')
file.close()
