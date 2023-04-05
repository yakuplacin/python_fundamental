# with automatically close after you have done with the file management.
with open("new_file2.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    # After reading the file, say it where your cursor should go. If you want to begin over, you can say it as 0.
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)
